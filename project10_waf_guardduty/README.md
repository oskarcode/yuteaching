# Project 10: Advanced Security with WAF & GuardDuty

## 🎯 Learning Objectives
By completing this project, you will:
- Understand AWS security services and defense-in-depth strategies
- Configure AWS WAF (Web Application Firewall) for application protection
- Enable and configure Amazon GuardDuty for threat detection
- Learn about security monitoring and incident response
- Implement security best practices for web applications
- Understand threat intelligence and anomaly detection
- Monitor security events and create automated responses

## 📋 Project Overview
This advanced security project demonstrates how to protect AWS resources using multiple layers of security. You'll configure WAF to protect web applications from common attacks and enable GuardDuty to detect malicious activity and threats in your AWS environment.

## 🏗️ Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│    Internet     │───▶│    AWS WAF       │───▶│   Application   │
│  (Attackers &   │    │ (Web Firewall)   │    │ Load Balancer   │
│   Legitimate    │    │ - Block IPs      │    │                 │
│    Traffic)     │    │ - Rate Limiting  │    │                 │
└─────────────────┘    │ - SQL Injection  │    └─────────────────┘
                       │ - XSS Protection │             │
                       └──────────────────┘             ▼
                                │                ┌─────────────────┐
                                ▼                │   Target Apps   │
                       ┌──────────────────┐     │ (EC2/ECS/etc.)  │
                       │   CloudWatch     │     └─────────────────┘
                       │   (WAF Logs)     │
                       └──────────────────┘
                                │
                                ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GuardDuty     │◀───│   VPC Flow Logs  │    │   CloudTrail    │
│ Threat Detection│    │   DNS Logs       │    │   API Logs      │
│ - Malware       │    │   Network Events │    │   User Activity │
│ - Crypto Mining │    └──────────────────┘    └─────────────────┘
│ - Reconnaissance│             │                       │
└─────────────────┘             ▼                       ▼
         │                ┌──────────────────┐    ┌─────────────────┐
         └───────────────▶│   EventBridge    │    │      SNS        │
                          │  (Automation)    │    │ (Notifications) │
                          └──────────────────┘    └─────────────────┘
```

## 🔧 AWS Services Used
- **AWS WAF**: Web Application Firewall
- **Amazon GuardDuty**: Threat detection service
- **CloudWatch**: Monitoring and logging
- **VPC Flow Logs**: Network traffic monitoring
- **CloudTrail**: API activity logging
- **SNS**: Security notifications
- **EventBridge**: Event-driven security automation

## 📝 Prerequisites
- Completed Projects 1-8
- Understanding of web security concepts
- Knowledge of common web attacks (OWASP Top 10)
- Familiarity with network security principles
- Running web application (from previous projects)

## 🚀 Implementation Methods

### Method 1: AWS Management Console (Recommended for Learning)

#### Step 1: Enable GuardDuty
1. Navigate to GuardDuty Console
2. Click "Get Started"
3. Enable GuardDuty:
   - 30-day free trial available
   - Enable for current region
   - Accept service-linked role creation
4. Review findings dashboard (initially empty)

#### Step 2: Configure VPC Flow Logs (Enhanced GuardDuty Detection)
```bash
# Enable VPC Flow Logs for better threat detection
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids vpc-12345678 \
  --traffic-type ALL \
  --log-destination-type cloud-watch-logs \
  --log-group-name VPCFlowLogs \
  --deliver-logs-permission-arn arn:aws:iam::account:role/flowlogsRole
```

#### Step 3: Create WAF Web ACL
1. Navigate to AWS WAF Console
2. Create Web ACL:
   - Name: `WebAppProtectionACL`
   - Resource type: Application Load Balancer
   - Associated resources: Select your ALB from previous projects

#### Step 4: Configure WAF Rules
**Rule 1: Rate Limiting**
1. Add rule → Rate-based rule
2. Configuration:
   - Name: `RateLimitRule`
   - Rate limit: 2000 requests per 5 minutes
   - Action: Block
   - Scope: All requests

**Rule 2: AWS Managed Rules**
1. Add managed rule groups:
   - `AWSManagedRulesCommonRuleSet` (OWASP Top 10)
   - `AWSManagedRulesKnownBadInputsRuleSet`
   - `AWSManagedRulesSQLiRuleSet` (SQL injection)
   - `AWSManagedRulesLinuxRuleSet` (if using Linux)

**Rule 3: Geographic Blocking (Optional)**
```yaml
# Block traffic from specific countries
Rule:
  Name: GeoBlockRule
  Statement:
    GeoMatchStatement:
      CountryCodes:
        - CN  # China
        - RU  # Russia
  Action: Block
```

**Rule 4: IP Reputation**
1. Add managed rule: `AWSManagedRulesAmazonIpReputationList`
2. Action: Block
3. This blocks known malicious IP addresses

#### Step 5: Configure WAF Logging
1. Enable logging for Web ACL
2. Destination: CloudWatch Logs
3. Log group: `aws-waf-logs-webappprotection`
4. Include/exclude specific fields as needed

#### Step 6: Create GuardDuty Custom Threat List (Optional)
```bash
# Create S3 bucket for threat intelligence
aws s3 mb s3://my-threat-intel-bucket-$(date +%s)

# Upload custom threat list (plain text file with IPs)
echo "192.0.2.1" > threat-list.txt
echo "198.51.100.1" >> threat-list.txt
aws s3 cp threat-list.txt s3://my-threat-intel-bucket/threat-list.txt

# Configure in GuardDuty Console:
# Lists → Threat lists → Add threat list
```

#### Step 7: Set Up Security Notifications
1. Create SNS Topic:
   - Name: `SecurityAlerts`
   - Subscribe your email for notifications

2. Create EventBridge Rule for GuardDuty findings:
```json
{
  "source": ["aws.guardduty"],
  "detail-type": ["GuardDuty Finding"],
  "detail": {
    "severity": [7.0, 8.9]  // High and medium severity
  }
}
```

#### Step 8: Test Security Controls
**WAF Testing:**
```bash
# Test rate limiting (run multiple times quickly)
for i in {1..100}; do
  curl -s https://your-alb-domain.com/ > /dev/null
  echo "Request $i sent"
done

# Test with suspicious user agent
curl -H "User-Agent: sqlmap/1.0" https://your-alb-domain.com/

# Test SQL injection attempt
curl "https://your-alb-domain.com/?id=1' OR '1'='1"
```

### Method 2: CloudFormation Template

```bash
# Deploy security infrastructure
aws cloudformation create-stack \
  --stack-name advanced-security-stack \
  --template-body file://project10_waf_guardduty.yaml \
  --parameters ParameterKey=LoadBalancerArn,ParameterValue=arn:aws:elasticloadbalancing:region:account:loadbalancer/app/name/id \
  --capabilities CAPABILITY_IAM
```

## 📁 Project Files

### `aws_ui_instructions.txt`
Step-by-step AWS Console instructions for manual security setup.

### `project10_waf_guardduty.yaml`
CloudFormation template that creates:
- GuardDuty detector with findings export
- WAF Web ACL with comprehensive rule set
- CloudWatch log groups for WAF logs
- SNS topic for security notifications
- EventBridge rules for automated responses

## 💰 Cost Estimation
- **GuardDuty**: $4.00 per million events analyzed + $0.50 per GB of flow logs
- **AWS WAF**: $1.00 per Web ACL + $0.60 per million requests
- **VPC Flow Logs**: $0.50 per GB published to CloudWatch
- **CloudWatch Logs**: $0.50 per GB ingested
- **SNS**: $0.50 per million notifications
- **Total Estimated Cost**: $20-50/month depending on traffic volume

## 🔍 Key Learning Points

### WAF Protection Layers
- **Rate Limiting**: Prevent DDoS and brute force attacks
- **Managed Rules**: Protection against OWASP Top 10
- **Custom Rules**: Business-specific security requirements
- **Geographic Filtering**: Block traffic from specific regions

### GuardDuty Threat Detection
- **Machine Learning**: Behavioral analysis and anomaly detection
- **Threat Intelligence**: Known malicious IPs and domains
- **DNS Analysis**: Detection of DNS-based attacks
- **Cryptocurrency Mining**: Detection of unauthorized mining

### Security Event Types GuardDuty Detects
- **Reconnaissance**: Port scanning, OS fingerprinting
- **Instance Compromise**: Cryptocurrency mining, malware
- **Account Compromise**: Credential compromise, privilege escalation
- **Bucket Compromise**: S3 data exfiltration, policy changes

## 🧪 Testing & Validation

### Verification Steps
1. ✅ GuardDuty enabled and generating findings
2. ✅ WAF Web ACL associated with load balancer
3. ✅ WAF rules blocking malicious requests
4. ✅ VPC Flow Logs feeding GuardDuty
5. ✅ Security notifications working
6. ✅ CloudWatch logs capturing security events

### Security Testing
```bash
# Generate GuardDuty findings (use carefully in test environment)
# Port scan detection
nmap -sS your-ec2-public-ip

# DNS tunneling simulation
dig @your-dns-server malicious-domain.com

# Check WAF metrics
aws wafv2 get-sampled-requests \
  --web-acl-arn arn:aws:wafv2:region:account:regional/webacl/name/id \
  --rule-metric-name RateLimitRule \
  --scope REGIONAL \
  --time-window StartTime=2025-01-01T00:00:00Z,EndTime=2025-01-01T01:00:00Z \
  --max-items 100
```

### Monitoring Commands
```bash
# View GuardDuty findings
aws guardduty list-findings --detector-id <detector-id>

# Get specific finding details
aws guardduty get-findings \
  --detector-id <detector-id> \
  --finding-ids <finding-id>

# Check WAF blocked requests
aws logs filter-log-events \
  --log-group-name aws-waf-logs-webappprotection \
  --filter-pattern '{ $.action = "BLOCK" }'
```

## 🚨 Troubleshooting

### Common Issues
1. **WAF blocking legitimate traffic**
   - Review WAF logs for false positives
   - Adjust rule sensitivity
   - Create allow rules for legitimate patterns

2. **GuardDuty not generating findings**
   - Ensure VPC Flow Logs are enabled
   - Check CloudTrail is logging API calls
   - Wait for baseline establishment (7-14 days)

3. **High WAF costs**
   - Review request volume and pricing
   - Optimize rules to reduce processing
   - Use sampling for logging

### Security Incident Response
```bash
# Example: Investigate suspicious IP
IP="192.0.2.1"

# Check WAF blocks
aws logs filter-log-events \
  --log-group-name aws-waf-logs-webappprotection \
  --filter-pattern "{ $.httpRequest.clientIp = \"$IP\" }"

# Check VPC Flow Logs
aws logs filter-log-events \
  --log-group-name VPCFlowLogs \
  --filter-pattern "$IP"

# Block IP in WAF
aws wafv2 update-ip-set \
  --scope REGIONAL \
  --id <ip-set-id> \
  --addresses $IP/32
```

## 🧹 Cleanup Instructions

### Manual Cleanup
1. Disable GuardDuty detector
2. Delete WAF Web ACL and rules
3. Delete CloudWatch log groups
4. Delete SNS topics and subscriptions
5. Delete EventBridge rules
6. Delete threat intelligence S3 bucket

### CloudFormation Cleanup
```bash
# Note: GuardDuty may need manual cleanup
aws guardduty delete-detector --detector-id <detector-id>

aws cloudformation delete-stack --stack-name advanced-security-stack
```

## 📚 Additional Resources
- [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/)
- [Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/)
- [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/)

## 🔧 Advanced Security Concepts
- **AWS Shield**: DDoS protection service
- **Security Hub**: Centralized security findings
- **Config**: Resource compliance monitoring
- **Macie**: Data classification and protection
- **Inspector**: Application vulnerability assessment

## 🔐 Security Best Practices Implemented
- **Defense in Depth**: Multiple security layers
- **Automated Response**: Event-driven security actions
- **Continuous Monitoring**: Real-time threat detection
- **Threat Intelligence**: Known bad actors and patterns
- **Incident Response**: Automated alerting and logging

## 📊 Security Metrics to Monitor
```bash
# WAF metrics
- Blocked requests count
- Allowed requests count
- Rule match counts

# GuardDuty metrics
- Finding counts by severity
- Finding types and frequency
- Mean time to detection

# General security metrics
- Failed authentication attempts
- Unusual API activity
- Network anomalies
```

## 🚀 Automation Examples
```python
# Lambda function for automated WAF IP blocking
import json
import boto3

def lambda_handler(event, context):
    wafv2 = boto3.client('wafv2')
    
    # Extract IP from GuardDuty finding
    finding = event['detail']
    malicious_ip = finding['service']['remoteIpDetails']['ipAddressV4']
    
    # Add to WAF IP set
    response = wafv2.update_ip_set(
        Scope='REGIONAL',
        Id='malicious-ips-set',
        Addresses=[f"{malicious_ip}/32"]
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Blocked IP: {malicious_ip}')
    }
```

## ➡️ Next Steps
After completing this project:
1. Explore AWS Security Hub for centralized security management
2. Implement AWS Config for compliance monitoring
3. Learn about Amazon Macie for data protection
4. Study incident response automation with Lambda
5. Explore container security with Amazon ECR scanning

---
**🎓 Congratulations!** You've successfully implemented advanced AWS security services and learned how to protect your applications from threats using WAF and GuardDuty. You now understand defense-in-depth security strategies and automated threat response.