After adding the appropriate values and commands,
1. Loaded the template into the stack
2. Set the ssh key
3. Created the stack

I logged into the server with the "ssh -i" command

I had an issue with the template where it rollback on the Route/Route table step. I did not know it was this issue. I decided to create a stack the old fashion way: I created a stack one step at a time.

I named the stack, click Next

I named the VPC, set 10.0.0.0/24. where when I typed /24, it told me that /24 is within the range with another vpc. I realized I forgot to remove the network resources from project 3. Once I did that, I reuploaded the template, the stack was created successfully.

Another thing I figured out was the software the post-installation of the stack was not installing.

I sshed into the instance and try installing the software manually. It said apt-get was not a command. I tried apt install, same response.

I looked at the ami that I selected and realized I chose the wrong ubuntu image.

I went to my main instance and copied the ami id, and I pasted it into the template.

I reloaded the template again and the commands worked. I was able to ssh and see all my commands installed