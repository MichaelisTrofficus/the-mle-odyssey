
Source: https://www.udemy.com/course/terraform-for-the-absolute-beginners

This is the traditional IT Infrastructure workflow. It took ages to deploy applications and also scaling up and down the application. Furthermore, this infrastructure was expensive,  error prone and wasted resources.

![[traditional_infra.png]]

But organisations have moved  to Cloud Providers in the last years. We are not going to enumerate all the Cloud advantages, but there's a clear disadvantage. Every team is generating code for infrastructure deployment automation. So, each team will have scripts in Python, JS, Go, Java, whatever, doing exactly the same! That's redundant, and that's also the reason for the appearance of IAC Tools.

![[iac_tools.png]]

Terraform is a **infrastructure provisioning tool**. One of it's major advantages is being able to deploy infrastructure in multiple platforms (providers).


>Providers are a logical abstraction of an upstream API. They are responsible for understanding API interactions and exposing resources.

Check this link to learn about available providers: https://registry.terraform.io/browse/providers

### How Terraform works

Terraform uses HCL, a **declarative language** (such as SQL, we declare the final state of the infrastructure and Terraform manages to create this infrastructure).  Terraform works in **three** phases: `init, plan, apply`.


![[init_plan_apply.png]]

### HCL Basics

An HCL file (`.tf` extension) has the following constituent blocks:

![[hcl_basics.png]]

Let's create a test document. First of all, we are going to create a test HCL file.

```hcl
resource "local_file" "test_document" {  
	filename = "./test_document.txt"  
	content = "This file was created by terraform :)"  
}
```

Now, run `terraform apply`.

![[Pasted image 20230612092645.png]]

This command will initialise the backend and download the plugins needed to configure the plan (in this case, just the plugin to work with local files) -> `hashicorp/local`.

If we want to see Terraform's plan, just run `terraform plan`.

![[Pasted image 20230612092921.png]]

Finally, to create the resource just run `terraform apply`, and the file will be created in the same directory. If you want to destroy the resource, simply run `terraform destroy`.



