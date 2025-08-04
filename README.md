# AWS Cloud Computing Teaching Projects 🚀

A comprehensive collection of hands-on AWS cloud computing projects designed for educational purposes. This repository contains 10 progressive projects that teach fundamental to advanced AWS concepts through practical implementation.

## 📚 Course Overview

These projects are designed to provide students with real-world experience in AWS cloud services, from basic account setup to advanced security and analytics implementations. Each project builds upon previous knowledge and introduces new AWS services and concepts.

## 🎯 Learning Objectives

By completing these projects, students will:
- Understand AWS fundamentals and best practices
- Gain hands-on experience with core AWS services
- Learn Infrastructure as Code (IaC) using CloudFormation
- Implement security, monitoring, and cost optimization strategies
- Deploy containerized applications and serverless functions
- Work with databases, networking, and content delivery networks

## 📋 Project Structure

| Project | Title | Key AWS Services | Difficulty |
|---------|-------|------------------|------------|
| [Project 1](./project1_set_up_aws_account/) | AWS Account Setup & Billing | CloudWatch, SNS | Beginner |
| [Project 2](./project2_iam_user_group_role/) | IAM Users, Groups & Roles | IAM | Beginner |
| [Project 3](./project3_install_aws_cli_and_s3_api/) | AWS CLI & S3 Operations | S3, CLI | Beginner |
| [Project 4](./project4_custom_vpc_ec2_webapp/) | Custom VPC & EC2 Web App | VPC, EC2, Security Groups | Intermediate |
| [Project 5](./project5_db_connect_write_read/) | Database Connectivity | RDS, EC2 | Intermediate |
| [Project 6](./project6_hostedzone_s3_cloudfront/) | CDN & Static Website | Route 53, S3, CloudFront | Intermediate |
| [Project 7](./project7_django_ecr_ecs/) | Containerized Django App | ECR, ECS, Fargate | Advanced |
| [Project 8](./project8_lambda_apigateway/) | Serverless API | Lambda, API Gateway | Advanced |
| [Project 9](./project9_alb_logs_athena/) | Load Balancer Analytics | ALB, S3, Athena | Advanced |
| [Project 10](./project10_waf_guardduty/) | Security & Threat Detection | WAF, GuardDuty | Advanced |

## 🛠️ Prerequisites

### Required Knowledge
- Basic understanding of cloud computing concepts
- Familiarity with command line interface
- Basic knowledge of web technologies (HTML, HTTP)
- Understanding of networking fundamentals

### Required Tools
- AWS Account (Free Tier eligible)
- AWS CLI installed and configured
- Text editor or IDE
- Web browser
- (Optional) Docker for containerization projects

## 🚀 Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/oskarcode/yuteaching.git
   cd yuteaching
   ```

2. **Follow the projects in order:**
   - Start with Project 1 to set up your AWS account
   - Each project folder contains detailed instructions
   - Use both AWS Console (UI) and CloudFormation templates

3. **Project Structure:**
   Each project folder contains:
   - `README.md` - Detailed project instructions and learning objectives
   - `aws_ui_instructions.txt` - Step-by-step AWS Console instructions
   - `*.yaml` - CloudFormation template for automated deployment
   - Additional files (Dockerfiles, source code, etc.) as needed

## 💡 How to Use These Projects

### For Students
1. Read the project README thoroughly
2. Try implementing using AWS Console first (UI instructions)
3. Then deploy using CloudFormation for automation experience
4. Experiment with configurations to deepen understanding
5. Clean up resources after each project to avoid charges

### For Instructors
- Each project is self-contained with clear learning objectives
- Projects build progressively in complexity
- Both manual (AWS Console) and automated (CloudFormation) approaches included
- Estimated completion times and cost estimates provided
- Can be used individually or as a complete course

## 💰 Cost Considerations

- Most projects utilize AWS Free Tier services
- Estimated costs provided in each project README
- Always clean up resources after completing projects
- Set up billing alerts (covered in Project 1)
- Monitor usage through AWS Cost Explorer

## 🔧 Deployment Methods

### Method 1: AWS Management Console
- Follow the `aws_ui_instructions.txt` in each project
- Best for learning and understanding AWS services
- More time-consuming but educational

### Method 2: CloudFormation (Infrastructure as Code)
- Use the provided `.yaml` templates
- Faster deployment and easier cleanup
- Industry best practice for infrastructure management

```bash
# Example CloudFormation deployment
aws cloudformation create-stack \
  --stack-name project-stack-name \
  --template-body file://project-template.yaml
```

## 📖 Additional Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to improve these educational materials.

## 📄 License

This project is provided for educational purposes. Please refer to AWS pricing and terms of service for any commercial usage.

## 🆘 Support

If you encounter issues:
1. Check the project-specific README for troubleshooting
2. Review AWS documentation for the services involved
3. Check AWS service status page for outages
4. Open an issue in this repository for help

---

**Happy Learning! 🎓**

*These projects are designed to provide hands-on experience with AWS services. Always follow AWS best practices and security guidelines in production environments.*