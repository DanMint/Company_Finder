resource "aws_s3_bucket" "example_bucket" {
  bucket = "my-unique-bucket-name-123456"
  force_destroy = true
}