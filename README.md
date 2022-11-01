## Deploy csi secrets in a new cluster

### source documentation: https://github.com/aws/secrets-store-csi-driver-provider-aws

#### 1. Install Secrets Store CSI driver:

```
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install -n kube-system csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver
```

#### 2. Install AWS Provider for CSI

```
helm repo add aws-secrets-manager https://aws.github.io/secrets-store-csi-driver-provider-aws
helm install -n kube-system secrets-provider-aws aws-secrets-manager/secrets-store-csi-driver-provider-aws
```

#### 3. create policy 

```
POLICY_ARN=$(aws --region us-east-2 --query Policy.Arn --output text iam create-policy --policy-name get-secrets-policy --policy-document '{
    "Version": "2012-10-17",
    "Statement": [ {
        "Effect": "Allow",
        "Action": ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],
        "Resource": ["arn:*:secretsmanager:*:*:secret:*"]
    } ]
}')
```

#### 4. Create the IAM OIDC provider for the cluster if you have not already done so:

```
eksctl utils associate-iam-oidc-provider --region="$REGION" --cluster="$CLUSTERNAME" --approve # Only run this once
```

#### 5. create IAM Service Account 

```
eksctl create iamserviceaccount --name getsecrets-$ENV --region="$REGION" --cluster "$CLUSTER_NAME" --namespace $ENV --attach-policy-arn "arn:aws:iam::$ACCOUNT_NUMBER:policy/get-secrets-policy" --approve --override-existing-serviceaccounts
```

#### 6. Deploy your app with mount from SecretProviderClass