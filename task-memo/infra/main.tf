provider "aws" {

   
    region = var.region
    profile = var.profile
  
}

module "sql_db" {
    
    source = "./db"
   
}
  