provider "aws" {
  version = "~> 2.0"
  region = "eu-west-2	
"
}

# ECS Task Definition
resource "aws_ecs_task_definition" "simulate_system_task" {
  family                   = "simulate-system-app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = <<DEFINITION
[
  {
    "name": "simulate-system-container",
    "image": "docker-image", 
    "cpu": 256,
    "memory": 512,
    "essential": true,
    "portMappings": [
      {
        "containerPort": 80,
        "hostPort": 80
      }
    ]
  }
]
DEFINITION
}

# AWS ECS Service
resource "aws_ecs_service" "simulate_system_service" {
  name            = "simulate-system-service"
  cluster         = "existing-ecs-cluster"  
  task_definition = aws_ecs_task_definition.simulate_system_task.arn
  launch_type     = "FARGATE"

  network_configuration {
    subnets = ["subnet-xxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyy"]  
    security_groups = ["sg-xxxxxxxxxxxxxxxxx"]  
  }

  depends_on = [aws_ecs_task_definition.simulate_system_task]
}
