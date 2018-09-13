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
    
.. method:: do_api_get(resourcePath, params=None, headers = None)
            
            Performs GET resource from resourcePath using Asset credentials
    
            :samp:`resourcePath` REST resource path within LiveIntersect

            :samp:`params` Http parameteres (query-string)

            :samp:`headers` Http headers
    
.. method:: do_api_post(resourcePath, jsonObj, headers = None)
            
            Performs POST to resourcePath using Asset credentials
            
            :samp:`resourcePath` REST resource path within LiveIntersect
            
            :samp:`jsonObj` JSON payload
            
            :samp:`headers` Http headers
    
.. method:: register_asset()
    
    Use this method to register your device and with the LiveIntersect server.  Every asset must be registered before the cloud accepts any communication from the device.
    This method first checks if asset instance is already registered, if not new registration request will be made.
    
.. method:: post_metric(asset)

        Use this method to retrieve information about the current asset.  This method will return the asset properties, configuration data (within attribute list), current telemetry data (within cloud)
        
        :samp:`asset` LiveIntersect Asset instance
        
        `returns` Api-Response JSON with JSON["result"] being asset-information
.. method:: post_metric(asset, metric_code, metric_value)

        Use this method to send sensor data or telemetry data to the LiveIntersect cloud.
        
        :samp:`asset` LiveIntersect Asset instance
        
        :samp:`metric_code` unique identifier for the metric associated with the asset type
        
        :samp:`metric_value` Raw value of the Metric (may contain unit-symbol i.e. 45C)
.. method:: post_attribute(asset, attr_code, attr_value)

        Use this method to configuration data to the LiveIntersect cloud. 
        Note: use get_asset_info to download attribute currently stored in the cloud.
        
        :samp:`asset` LiveIntersect Asset instance
        
        :samp:`attr_code` unique identifier for the attributes associated with the asset type
        
        :samp:`attr_value` Raw value of the attribute (may contain unit-symbol i.e. 45C)
