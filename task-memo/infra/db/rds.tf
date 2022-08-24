resource "aws_db_subnet_group" "db_sub_grp" {
    name = "db_sub_grp"
    subnet_ids = ["subnet-06581c75c5cfe457e","subnet-0c476c5a941be2765"]
    
  
}

resource "random_password" "random_pass" {

    length = 8
    special = true
    override_special = "_!%^"
}

    
resource "aws_secretsmanager_secret" "password" {
  name = "demo-db-password"
}


resource "aws_secretsmanager_secret_version" "password" {

  secret_id = aws_secretsmanager_secret.password.id
  secret_string = random_password.random_pass.result
}


resource "aws_db_instance" "demo_db" {

    db_name = "demo_db"
    engine = "mysql"
    engine_version = "8.0.27"
    instance_class = "db.t2.micro"
    identifier = "demo-db"
    username = "demo"
    password = aws_secretsmanager_secret_version.password.secret_string

    allocated_storage = 20
    multi_az = false
    storage_type = "gp2"
    availability_zone = "us-west-2a"
    db_subnet_group_name = aws_db_subnet_group.db_sub_grp.name
    publicly_accessible = true
    vpc_security_group_ids = ["sg-0f6df78083b31fc9a"]
    skip_final_snapshot = true
    

  
}

output "db_endpoint" {

    value = aws_db_instance.demo_db.endpoint
    
}
  
