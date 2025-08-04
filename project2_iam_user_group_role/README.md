# Project 2: IAM Users, Groups, and Roles

## 🎯 Learning Objectives
By completing this project, you will:
- Understand AWS Identity and Access Management (IAM) fundamentals
- Create and manage IAM users, groups, and roles
- Implement the principle of least privilege
- Learn about AWS security best practices
- Understand the difference between users, groups, and roles
- Configure programmatic and console access

## 📋 Project Overview
This project introduces you to AWS IAM, the foundation of AWS security. You'll create IAM users for human access, groups for permission management, and roles for AWS services to interact with each other securely.

## 🏗️ Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   IAM User      │───▶│   IAM Group      │───▶│  IAM Policies   │
│  (BasicUser)    │    │ (BasicViewGroup) │    │ (ReadOnlyAccess)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐    ┌──────────────────┐
│   IAM Role      │───▶│  Trust Policy    │
│ (ExampleRole)   │    │ (EC2 Service)    │
└─────────────────┘    └──────────────────┘
```

## 🔧 AWS Services Used
- **IAM (Identity and Access Management)**: Core service for authentication and authorization
- **CloudFormation**: Infrastructure as Code for automated deployment

## 📝 Prerequisites
- Completed Project 1 (AWS Account Setup)
- Root account access to AWS Management Console
- Understanding of basic security concepts

## 🚀 Implementation Methods

### Method 1: AWS Management Console (Recommended for Learning)

#### Step 1: Create IAM Group
1. Navigate to IAM service in AWS Console
2. Go to "User groups" → "Create group"
3. Name: `BasicViewGroup`
4. Attach policies:
   - `ReadOnlyAccess` (AWS managed policy)
   - Or create custom policy for specific permissions
5. Create the group

#### Step 2: Create IAM User
1. Go to "Users" → "Add users"
2. Username: `BasicUser`
3. Access type:
   - ✅ AWS Management Console access
   - ✅ Programmatic access (optional)
4. Set console password (auto-generated or custom)
5. Add user to `BasicViewGroup`
6. Review and create user
7. **Important**: Download credentials CSV file

#### Step 3: Create IAM Role
1. Go to "Roles" → "Create role"
2. Trusted entity: "AWS service"
3. Use case: "EC2"
4. Attach policies:
   - `ReadOnlyAccess` or custom policy
5. Role name: `ExampleRole`
6. Create role

#### Step 4: Test and Verify
1. Sign out from root account
2. Sign in as the new IAM user
3. Test permissions (should have read-only access)
4. Verify role can be assumed by EC2 instances

### Method 2: CloudFormation Template

```bash
# Deploy IAM resources
aws cloudformation create-stack \
  --stack-name iam-basic-setup \
  --template-body file://project2_iam_user_group_role.yaml \
  --capabilities CAPABILITY_IAM
```

## 📁 Project Files

### `aws_ui_instructions2.txt`
Step-by-step AWS Console instructions for manual setup.

### `project2_iam_user_group_role.yaml`
CloudFormation template that creates:
- IAM Group with ReadOnly permissions
- IAM User and adds to group
- IAM Role for EC2 services
- Custom policies (if needed)

## 💰 Cost Estimation
- **IAM Users, Groups, Roles**: Free
- **CloudFormation Stack**: Free
- **Total Estimated Cost**: $0

## 🔍 Key Learning Points

### IAM Fundamentals
- **Users**: Represent people or applications that need AWS access
- **Groups**: Collections of users with similar permission requirements
- **Roles**: Can be assumed by AWS services or trusted entities
- **Policies**: JSON documents that define permissions

### Security Best Practices
- **Principle of Least Privilege**: Grant only necessary permissions
- **Use Groups**: Assign permissions to groups, not individual users
- **Regular Reviews**: Periodically audit IAM permissions
- **Strong Passwords**: Enforce password policies
- **MFA**: Enable multi-factor authentication

### Access Types
- **Console Access**: Web browser access to AWS Management Console
- **Programmatic Access**: API/CLI access using access keys
- **Temporary Credentials**: Using roles and STS tokens

## 🧪 Testing & Validation

### Verification Steps
1. ✅ IAM group created with appropriate policies
2. ✅ IAM user created and added to group
3. ✅ User can sign in to AWS Console
4. ✅ User has read-only permissions (cannot create resources)
5. ✅ IAM role created and can be assumed by EC2
6. ✅ All resources visible in IAM dashboard

### Test Scenarios
```bash
# Test programmatic access (if enabled)
aws sts get-caller-identity

# Test assuming a role
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT-ID:role/ExampleRole \
  --role-session-name test-session
```

## 🚨 Troubleshooting

### Common Issues
1. **User cannot sign in**
   - Check username and password
   - Verify console access is enabled
   - Check account ID is correct

2. **Access denied errors**
   - Verify user is in correct group
   - Check group has appropriate policies
   - Review policy permissions

3. **CloudFormation fails**
   - Ensure you have CAPABILITY_IAM flag
   - Check for existing resources with same names
   - Verify sufficient permissions to create IAM resources

### Security Considerations
- Never share root account credentials
- Use temporary credentials where possible
- Regularly rotate access keys
- Monitor IAM usage with CloudTrail

## 🧹 Cleanup Instructions

### Manual Cleanup
1. Delete IAM user (remove from groups first)
2. Delete IAM group
3. Delete IAM role
4. Remove any custom policies

### CloudFormation Cleanup
```bash
# Delete the stack
aws cloudformation delete-stack --stack-name iam-basic-setup

# Verify deletion
aws cloudformation describe-stacks --stack-name iam-basic-setup
```

## 📚 Additional Resources
- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)
- [IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)

## 🔐 Security Reminders
- **Never hardcode credentials** in code or configuration files
- **Use IAM roles** for applications running on AWS services
- **Enable CloudTrail** to monitor IAM activities
- **Set up password policies** for console users
- **Regular access reviews** to ensure permissions are still needed

## ➡️ Next Steps
After completing this project:
1. Proceed to [Project 3: AWS CLI & S3 Operations](../project3_install_aws_cli_and_s3_api/)
2. Practice creating different types of policies
3. Explore IAM Access Analyzer for permission insights
4. Consider enabling AWS Organizations for multi-account management

---
**🎓 Congratulations!** You've successfully implemented AWS IAM fundamentals and understand the core security model that protects AWS resources.