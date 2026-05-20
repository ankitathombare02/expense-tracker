provider "aws" {
  region = "ap-south-1"
}

# ✅ Security Group
resource "aws_security_group" "web_sg" {
  name        = "expense-app-sg"
  description = "Allow SSH, HTTP, Django ports"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Django App"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # ✅ Outbound
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "expense-app-sg"
  }
}

# ✅ EC2 Instance
resource "aws_instance" "django_server" {
  ami           = "ami-03f4878755434977f"
  instance_type = "t3.small"   # ✅ Working

  key_name = "expense-key"

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  associate_public_ip_address = true

  # ✅ This ensures better SSH compatibility
  metadata_options {
    http_tokens = "optional"
  }

  tags = {
    Name = "ExpenseTrackerServer"
  }
}

# ✅ Output
output "public_ip" {
  value = aws_instance.django_server.public_ip
}