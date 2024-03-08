# cs415_website Install Notes

## EC2 Install Commands
## Ubuntu
- Allow Inbound Rules
  - SSH
  - HTTP
  - HTTPS
- Attach IAM Role to Instance
- User Data
    ```
    #!/bin/bash
    sudo apt update -y
    sudo apt install ruby wget -y
    cd /home/ubuntu
    sudo wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
    sudo chmod +x ./install
    sudo ./install auto
    sudo apt install -y apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```
## SSH into the Instance
- Validate CodeDeploy Agent is installed and running:
  `sudo service codedeploy-agent status`
- Validate Apache is installed and running:
  `sudo systemctl status apache2`

## Deploy Notes
- Deploy build files into:
  `/var/www/html/`



<Route path="/modules/1" element={<Module1 />} />
            <Route path="/modules/2" element={<Module2 />} />
            <Route path="/modules/3" element={<Module3 />} />
            <Route path="/modules/4" element={<Module4 />} />
            <Route path="/modules/5" element={<Module5 />} />
            <Route path="/modules/6" element={<Module6 />} />


<Link to="/login" style={{ padding: 5 }}>Login</Link>
            <Link to="/userprofile" style={{ padding: 5 }}>User Profile</Link>
            <Link to="/users" style={{ padding: 5 }}>Users</Link>
            <Link to="/modules/1" style={{ padding: 5 }}>Module 1</Link>
            <Link to="/modules/2" style={{ padding: 5 }}>Module 2</Link>
            <Link to="/modules/3" style={{ padding: 5 }}>Module 3</Link>
            <Link to="/modules/4" style={{ padding: 5 }}>Module 4</Link>
            <Link to="/modules/5" style={{ padding: 5 }}>Module 5</Link>
            <Link to="/modules/6" style={{ padding: 5 }}>Module 6</Link>