from aws_cdk import Stack
from constructs import Construct
 
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecs_patterns
 
 
class conductorFastAPIStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
 
        self.vpc = ec2.Vpc(self, "MyConductorVPC", max_azs=3)
 
        self.ecs_cluster = ecs.Cluster(
            self,
            "MyConductorECSCluster",
            vpc=self.vpc,
        )
 
        image = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=ecs.ContainerImage.from_asset(
                directory="../src",
            )
        )
 
        self.ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "MyConductorFastAPIService",
            cluster=self.ecs_cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=2,
            task_image_options=image,
        )
 

