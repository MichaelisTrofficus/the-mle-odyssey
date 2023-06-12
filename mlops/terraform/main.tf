resource "local_file" "test_document" {
  filename = "./test_document.txt"
  content = "This file was created by terraform :)"
  file_permission = "0700"
}
