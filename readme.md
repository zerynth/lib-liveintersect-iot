LiveIntersect Asset Simulation
==============================

LiveIntersect library and reference implementation for Zerynth Embedded firmware

## Prerequisite
1. Zerynth Studio r2.1.1-p01
1. ESP32 DevKitC (Or other compatible hardware)

## LiveIntersect IOT-Core-Asset [iot.py](iot.py)
Implementation of Live-Intersect core http implementations

1. Register-Asset register_asset()
1. LiveIntersect API GET do_api_get()
1. LiveIntersect API POST do_api_post()
1. get_asset_info()
1. post_metric()
1. post_attribute()

## Example Implementation
### LiveIntersect Asset Configuration [examples/Asset_Simulation/asset.config.json](examples/Asset_Simulation/asset.config.json)
LiveIntersect Asset configuration

1. baseUrl
1. apiKey
1. srNo
1. assetName
1. assetTypeCode

### LiveIntersect Helper [examples/Asset_Simulation/helper.py](examples/Asset_Simulation/helper.py)
Helper Library (helper.py) to access Asset Configuration & IOT-Core functions

1. load_asset_conf()

### LiveIntersect Asset Simulation [examples/Asset_Simulation/main.py](examples/Asset_Simulation/main.py)
Reference implementation of LiveIntersect Asset implementation