import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/counter', methods=['POST'])
def handle_counter():
    try:
        # Pull connection key securely from environment
        conn_str = os.environ.get('AZURE_COSMOS_CONNECTION')
        if not conn_str:
            return jsonify({"count": 999, "error": "Missing Connection String"}), 200
            
        from azure.cosmos import CosmosClient
        client = CosmosClient.from_connection_string(conn_str)
        database = client.get_database_client("ResumeDB")
        container = database.get_container_client("CounterContainer")
        
        # Read item '1' using its partition key '1'
        item = container.read_item(item="1", partition_key="1")
        item['count'] += 1
        container.replace_item(item=item, body=item)
        count = item['count']
    except Exception as e:
        print(f"Cosmos DB Error: {str(e)}")
        count = 1
        
    return jsonify({"count": count}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)