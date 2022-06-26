import os
import aws_cdk as cdk
from conductorFastapi import conductorFastAPIStack

app = cdk.App()
conductorFastAPIStack(app, "FastAPIStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )
app.synth()