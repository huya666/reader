import express from 'express';
import axios from 'axios';
import config from './config';
import cors from 'cors';

const app = express();

app.use(cors());

app.use((req, res, next) => {
//判断路径
  if(req.path !== '/' && !req.path.includes('.')){
    res.set({
      'Access-Control-Allow-Credentials': true, //允许后端发送cookie
      'Access-Control-Allow-Origin': req.headers.origin || '*', //任意域名都可以访问,或者基于我请求头里面的域
      'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type', //设置请求头格式和类型
      'Access-Control-Allow-Methods': 'PUT,POST,GET,DELETE,OPTIONS',//允许支持的请求方式
      'Content-Type': 'application/json; charset=utf-8'//默认与允许的文本格式json和编码格式
    })
  }
  req.method === 'OPTIONS' ? res.status(204).end() : next()
})

app.get('/', (req, res) => {
	res.json({ success: true })
})

app.get('/search', async (req, res) => {
	const { query } = req;

	const result = await axios.get(config.pyhost, );

	res.json({ success: true, ...result.data });
})

app.listen(config.port, () => {
	console.log('express app listening at 7200')
})