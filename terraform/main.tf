provider "aws" {
  region = "ap-south-1"
}

# ✅ Security Group
resource "aws_security_group" "web_sg" {
  name        = "expense-app-sg"
  description = "Allow SSH, HTTP, and App access"

  # ✅ SSH
  ingress {
    description = "SSH Access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # ✅ HTTP
  ingress {
    description = "HTTP Web"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # ✅ Django App
  ingress {
    description = "Django App"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # ✅ Outbound
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "expense-app-sg"
  }
}

# ✅ Amazon Linux EC2
resource "aws_instance" "django_server" {
  ami           = "ami-07a00cf47dbbc844c"   # ✅ Amazon Linux (FIXED)
  instance_type = "t3.micro"

  key_name = "expense-final"

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  associate_public_ip_address = true

  metadata_options {
    http_tokens = "optional"
  }

  tags = {
    Name = "expense-tracker"
  }
}

# ✅ Output Public IP
output "public_ip" {
  description = "Public IP of EC2"
  value       = aws_instance.django_server.public_ip
}