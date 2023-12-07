from qlik_sdk import (
    Apps, 
    Config, 
    AuthType, 
    GenericDimensionProperties, 
    NxLibraryDimensionDef,
    NxInfo,
    GenericMeasureProperties,
    NxLibraryMeasureDef
)

"""
Tenant
"""
base_url = 'https://{your tenant}.eu.qlikcloud.com'
api_key = '{your qlik api key}'

"""
Setting Up Config
"""
conf = Config(host=base_url, auth_type=AuthType.APIKey, api_key=api_key)

AppsObject =Apps(conf)
atscale_app = AppsObject.get('your app id')

dim_properties     = GenericDimensionProperties(qDim=NxLibraryDimensionDef(qFieldDefs=['Order Year', 'Order Quarter', 'Order Month'], qFieldLabels=[], qGrouping='H', qLabel="This text should be in the Name of the Master Element. But does not appear.", qLabelExpression="AtScaleDim"), qInfo=NxInfo( qType='dimension'))

with atscale_app.open():

    atscale_app.create_dimension(dim_properties)

measure_properties     = GenericMeasureProperties(qDim=NxLibraryMeasureDef(qActiveExpression=1, qDef="This text should be in the Name of the Master Element. But does not appear.", qGrouping="H", qLabel="This text should be in the Name of the Master Element. But does not appear." ), qInfo=NxInfo( qType='measure'))

with atscale_app.open():

    atscale_app.create_measure(measure_properties)
