from flask import  Flask,render_template,request
import boto3

app=Flask(__name__)





@app.route('/',methods=['GET'])
def index():
    if request.method=='GET':
        # l1=[]
        # l2=[]
        client=boto3.client('ec2')
        res=client.describe_instances()
        #=for i in res['Reservations']:
            #for j in i['Instances']:
                #for k in j['Tags']:
                   #= l1.append(k['Value']),l2.append(j['InstanceId'])
    return render_template('index.html',l1=res)

if __name__=="__main__":
    app.run(debug=True,use_reloader=True,host='0.0.0.0',port=80)

3