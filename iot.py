import requests
import json
import base64

REGISER_API = "/agentapi/registration"
ASSETS_API = "/agentapi/assets"
METRICS_API = "/agentapi/assetmetrics"
ATTRIBUTES_API = "/agentapi/assetattributes"

class Asset:
    """
================
The Asset class
================

.. class:: Asset(baseUrl, apiKey, srNo, assetName, assetTypeCode, ssl_ctx)

    This class represents asset software which facilitates all communication to the LiveIntersect cloud.  `LiveIntersect <https://esprida.com/platform/>`_ is a IoT enablement platform which collects and manages asset data and enables you to build IoT solutions.
	
	:samp:`baseUrl` url to LiveIntersect hosting, If you are using first implementation use `Sandbox Environment <https://sandbox.liveintersect.com>`_
	
	:samp:`apiKey` A valid API key representing an organization. If a API key has been generated following `LiveIntersect <https://sandbox.liveintersect.com/ui/faces/service/developer.xhtml?viewName=manage.api.key>`_
	
	:samp:`srNo` A hardware identifier (serial number) which unique within your Organization
	
	:samp:`assetName` User friendly name for this Asset (does not need to be unique)
	
	:samp:`assetTypeCode` Optional asset-type-code representing asset-type configured in in LiveIntersect environment
	
	:samp:`ssl_ctx` initialize SSL context please read `Zerynth Documentation <https://docs.zerynth.com/latest/official/core.zerynth.stdlib/examples/examples.html?highlight=secure%20http#core-zerynth-stdlib-secure-http>`_
    
	Example
	-------
    my_Asset = li_http.Asset(`https://liveintersect.com/`, apiKey, srNo, assetName, assetTypeCode, ssl_ctx)
    """
    def __init__(self, baseUrl, apiKey, srNo, assetName, assetTypeCode=None, ssl_ctx=None):
        self.baseUrl = baseUrl
        self.ssl_ctx = ssl_ctx
        self.apiKey = apiKey
        self.assetTypeCode = assetTypeCode
        self.srNo = srNo
        self.assetName = assetName
        self.assetId = ""
        self.assetLogin = ""

    def do_api_get(self, resourcePath, params=None, headers = None):
        """
    .. method:: do_api_get(resourcePath, params=None, headers = None)
		
		Performs GET resource from resourcePath using Asset credentials
	
		:samp:`resourcePath` REST resource path within LiveIntersect

		:samp:`params` Http parameteres (query-string)

		:samp:`headers` Http headers
        """
        if(self.assetLogin != ""):
            headers = {
                "Authorization": "Basic " + base64.standard_b64encode(self.assetLogin + ":")
            }
        response = requests.get(self.baseUrl + resourcePath, params=params, headers=headers, ctx=self.ssl_ctx)
        if(response.status >= 200 and response.status < 300):
            return json.loads(response.content)
        print(response.content)
        raise Exception

    def do_api_post(self, resourcePath, jsonObj, headers = None):
        """
    .. method:: do_api_post(resourcePath, jsonObj, headers = None)
		
		Performs POST to resourcePath using Asset credentials
		
		:samp:`resourcePath` REST resource path within LiveIntersect
		
		:samp:`jsonObj` JSON payload
		
		:samp:`headers` Http headers
        """
        if(self.assetLogin != ""):
            headers = {
                "Authorization": "Basic " + base64.standard_b64encode(self.assetLogin + ":")
            }
        response = requests.post(self.baseUrl + resourcePath, headers=headers, json=jsonObj, ctx=self.ssl_ctx)
        if(response.status >= 200 and response.status < 300):
            return json.loads(response.content)
        print(response.content)
        raise Exception

    def register_asset(self):
        """
    .. method:: register_asset()
	
        Use this method to register your device and with the LiveIntersect server.  Every asset must be registered before the cloud accepts any communication from the device.
        This method first checks if asset instance is already registered, if not new registration request will be made.
        """
        try:
            params = { 
                "apiKey" : self.apiKey,
                "srNo" : self.srNo
            }
            api_response = self.do_api_get(REGISER_API, params=params)
        except Exception as e:
            registration_data = {
                "apiKey": self.apiKey,
                "srNo": self.srNo,
                "assetName": self.assetName,
                "assetTypeCode": self.assetTypeCode
            }
            api_response = self.do_api_post(REGISER_API, registration_data)
        self.assetLogin = api_response["result"]["assetLogin"]
        self.assetId = api_response["result"]["assetId"]
        
def get_asset_info(asset):
    """
	.. method:: post_metric(asset)

		Use this method to retrieve information about the current asset.  This method will return the asset properties, configuration data (within attribute list), current telemetry data (within cloud)
		
		:samp:`asset` LiveIntersect Asset instance
		
		`returns` Api-Response JSON with JSON["result"] being asset-information
    """
    return asset.do_api_get(ASSETS_API + "/" + asset.assetId)

def post_metric(asset, metric_code, metric_value):
    """
	.. method:: post_metric(asset, metric_code, metric_value)
	
		Use this method to send sensor data or telemetry data to the LiveIntersect cloud.
		
		:samp:`asset` LiveIntersect Asset instance
		
		:samp:`metric_code` unique identifier for the metric associated with the asset type
		
		:samp:`metric_value` Raw value of the Metric (may contain unit-symbol i.e. 45C)
    """
    metricMsg = [{
            "metrics":[{
                "metricCode":metric_code,
                "values":[{
                    "metricValue": metric_value
                }]
            }]
        }]
    api_response = asset.do_api_post(METRICS_API , jsonObj=metricMsg)
    
def post_attribute(asset, attr_code, attr_value):
    """
	.. method:: post_attribute(asset, attr_code, attr_value)
	
		Use this method to configuration data to the LiveIntersect cloud. 
		Note: use get_asset_info to download attribute currently stored in the cloud.
		
		:samp:`asset` LiveIntersect Asset instance
		
		:samp:`attr_code` unique identifier for the attributes associated with the asset type
		
		:samp:`attr_value` Raw value of the attribute (may contain unit-symbol i.e. 45C)
    """
    attributeMsg = [{ 
        "attributeCode" : attr_code, "attributeValue" : attr_value
    }]
    api_response = asset.do_api_post(ATTRIBUTES_API , jsonObj=attributeMsg)
