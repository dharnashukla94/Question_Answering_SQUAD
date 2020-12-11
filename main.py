
from flask import Flask,request, render_template
from models.bert import bert
from models.robert import robert
from models.mobile_bert import mobilebert
from models.squeezebert import squeezebert

app = Flask("Normal_fuc")

@app.route("/" , methods=['GET', 'POST'])
def index():
	# Main page
	if request.method == 'POST':
		question = request.form['question']
		context = request.form['context']

		ans_bert = bert(question, context)
		ans_robert = robert({
		    'context': context,
		    'question': question
		})
		ans_mobile = mobilebert({
		    'context': context,
		    'question': question
		})
		ans_squeeze = squeezebert({
		    'context': context,
		    'question': question
		})
		ans_bert = {'answer':ans_bert,
					'score':0,
					'name':'BERT'	}
		ans_robert['name'] = 'RoBERT'
		ans_mobile['name'] = 'Mobile_Bert'
		ans_squeeze['name'] = 'Squeeze_Bert'			
		output = [ans_bert,ans_robert,ans_mobile,ans_squeeze]

		return render_template('index.html', output = output)

	return render_template('index.html')

if __name__ =='__main__':
   app.run(debug = "True" , host = "0.0.0.0", port=9090)
