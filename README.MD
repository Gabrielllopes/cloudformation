Este repositórico contem exemplos de como criar recursos na AWS utilizando CloudFormation.

É criada uma fila SQS que consome de um tópico SNS, uma função lambda vai ler desta fila e escrever em uma tabela DynamoBD toda vez que uma nova mensagem for publicada no tópico.

<img src=/img/flx.png>

Este reposiório é inspirado na série de vídeos [AWS: Aplicação orientada a eventos](https://www.youtube.com/watch?v=Q_S-dH57zmA) que ensina a fazer isso usando a interface gráfica da AWS. Aqui sera utilizado apenas CLI e CLoud formations.

A pasta `idividual` contem o yaml de como criar os recursos individualmente, equanto o `all_stack.yaml` cria todos os recursos de uma vez só.

Para que `all_stack` funcione é necessário que a função lambda seja compactada e colocada dentro de um bucket S3. 

Para compactar a função navegue até a pasta deste repositório e uilize o comando a seguir:

```bash
zip func_lambda.zip func_lambda.py
```

Para criar um bucket s3 e mover arquivo:

```bash
# Cria Bucket
aws s3 mb s3://<NOME DO SEU BUCKET>
# Move arquivo
aws s3 cp func_lambda.zip s3://<NOME DO SEU BUCKET>
```

Para executar o cloud formation por cli é necessário 2 passos:  
1. Trocar o nome do buckt que esta na linha 70 para o nome do seu bucket.  
2. Fazer upload do arquivo `all_stack.yaml` para o seu bucket.  

```bash
aws --region <REGIÃO DO SEU BUCKET> cloudformation create-stack --stack-name "oneForAll" --template-url "https://<NOME DO SEU BUCKET>.s3.amazonaws.com/all_stack.yaml" --capabilities CAPABILITY_NAMED_IAM
```