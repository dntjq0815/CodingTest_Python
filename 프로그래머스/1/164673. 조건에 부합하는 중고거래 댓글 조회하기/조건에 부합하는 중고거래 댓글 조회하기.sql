-- 코드를 입력하세요
SELECT bo.title, bo.board_id, 
re.reply_id, re.writer_id, re.contents, 
date_format(re.created_date, '%Y-%m-%d') as created_date
from used_goods_board as bo join used_goods_reply as re
on bo.board_id=re.board_id
where year(bo.created_date)=2022 and month(bo.created_date)=10
order by created_date, bo.title