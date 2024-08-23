import boto3

s3_client = boto3.client('s3')

def query_s3_select(bucket_name, key, query):
    try:
        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=key,
            ExpressionType='SQL',
            Expression=query,
            InputSerialization={
                'CSV': {
                    "FileHeaderInfo": "USE",
                    "FieldDelimiter": ";",
                    "QuoteCharacter": "\""
                }
            },
            OutputSerialization={'JSON': {}},
        )

        # Process the payload
        for event in response['Payload']:
            if 'Records' in event:
                print(event['Records']['Payload'].decode('utf-8'))
            elif 'Stats' in event:
                print("Processed Bytes:", event['Stats']['Details']['BytesProcessed'])
            elif 'End' in event:
                print("End of file")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    bucket_name = 'bucket-operacoes-policiais'
    object_name = 'PALAS_OPERACOES_2024_01_corrigido.csv'
    query_file = 'query.sql'

    with open(query_file, 'r', encoding='utf-8') as file:
        query = file.read()
        
    query_s3_select(bucket_name, object_name, query)
