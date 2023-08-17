import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Functions and Derivatives')


st.header(':chart_with_upwards_trend: :violet[**Functions**] and Their :violet[**Derivatives**] :chart_with_upwards_trend:')
st.caption('ในหัวข้อนี้เราจะมาเรียนรู้กันว่า :blue[ฟังก์ชัน] และ :blue[อนุพันธ์ของฟังก์ชัน] คืออะไร')

content = st.columns(2)
content[0].markdown(
    '''
:orange[**Contents**]
1. แนวคิดของฟังก์ชัน
2. กราฟของฟังก์ชัน
3. อัตราเร็วและความเร็วเฉลี่ย
'''
)
with content[1]:
    add_vertical_space(2)
content[1].markdown(
    '''
4. Limit และ ความเร็วชั่วขณะ
5. The Derived Function (Derivatives)
6. การหา Derivatives ของ Polynomials
'''
)
st.divider()

topic_list = [':green[**แนวคิดของฟังก์ชัน**]',':green[**กราฟของฟังก์ชัน**]',':green[**อัตราเร็วและความเร็วเฉลี่ย**]',
              ':green[**Limit และ อัตราเร็วชั่วขณะ**]',':green[**The Derived function (Derivatives)**]',':green[**Derivatives ของ Polynomials**]']

topic=[]
for i in range(len(topic_list)):
    topic.append(st.expander(topic_list[i]))
    topic[i].write('remove later . . .')


with topic[0]:
    st.markdown(
        '''
* :violet[**Set**]   

ในคณิตศาสตร์ เวลาที่เราเอา Objects มากองรวมๆกัน เราเรียกทั้งกองนั้นว่า :violet[**Set**] เช่น    
$A=\{ หมา, แมว, เป็ด, ไก่, . . . \}=\{ x| x = สัตว์\} $ อ่านว่า :green[A คือเซตของ $x$ เมื่อ $x$ คือสัตว์]   
$B=\{ ส้ม, แดง, เขียว, น้ำเงิน, . . .\}=\{y|y = สี \} $ อ่านว่า :green[B คือเซตของ $y$ เมื่อ $y$ คือสี]   
เซตบางตัวที่เจอบ่อย ควรรู้จักชื่อไว้ . . .   
:blue[**Natural Number**] : $\\N= \{ 1,2,3,4,5,6,... \}$    
:blue[**Interger**]: $\\Z= \{ ...,-3,-2,-1,0,+1,+2,+3,...\}$    
:blue[**Real Number**]: $\\R= \{ จำนวนจริง \}$    

* :violet[**Relations**]      
   
เมื่อเรามี Set แล้ว สิ่งถัดมาที่เราอาจจะอยากได้คือ ***อะไรสักอย่างที่โยงเซตสองเซตเข้าด้วยกัน*** ในคณิตศาสตร์เราเรียกสิ่งนั้นว่า :violet[**Relation, ความสัมพันธ์**]   
เช่น เราอาจจะสร้าง Relation ระหว่าง Set A กับ B ได้โดยนิยาม Relation จาก A ไป B ให้เป็น :orange[โยงสัตว์เข้ากับสีของมัน]   
หมา อาจมีสี ขาว ดำ เทา เพราะฉะนั้น จะได้ :green[$หมา \mapsto ขาว, ดำ, เทา$]   
แมว อาจมี แมวขาว แมวดำ แมวส้ม แมวเทา จะได้ :green[$แมว \mapsto ขาว, ดำ, ส้ม, เทา$]   

* :violet[**Functions**]      
   
จะเห็นว่า Relation ก็มีประโยชน์แล้ว มันใช้โยงสองสิ่งเข้าด้วยกัน แต่ว่าในฟิสิกส์(วิทยาศาสตร์) ถ้าใช้ Relation ไปเลยมันอาจจะเกิดปัญหาแปลกๆแบบนี้   
สมมุติเราอยากทำนายว่า ที่เวลาต่างๆลูกบอลอยู่ที่ไหน เราให้ :green[$t = \{ 1,2,3,...\}$] แทนเวลาต่างๆ ที่เราอยากทำนาย และเราให้
:green[$ x = \{ ...,-2,-1,0,1,2,... \}$] แทนตำแหน่งต่างๆที่เป็นไปได้ เพราะฉะนั้น เราควรสร้างความสัมพันธ์ที่โยง :green[$\\;t$, เวลา] เข้ากับ :green[$\\;x$, ตำแหน่ง]   
แต่ว่าถ้าเราอยากทำนายอนาคต มันควรมีข้อจำกัดดังนี้
1. ถ้าเราเลือกเวลามา 1 ตัว เราควรได้ตำแหน่งแค่ตำแหน่งเดียว :orange[$1\\;input \mapsto 1\\;output$] ไม่งั้นมันจะเกิดกรณีที่เราเลือกเวลามาหนึ่งตัว แต่ได้หลายตำแหน่ง ก็คือเราทำนายอนาคตไม่ได้นั่นเอง
2. เซต :green[$\\;t\\;$] แทนเวลาที่เราอยากทำนาย เพราะฉะนั้น :orange[ทุกตัวใน $\\;t\\;$ ควรเข้าร่วมกับ Relation นี้] ไม่งั้นจะกลายเป้นว่ามีบางเวลาที่ไม่ได้เข้าร่วม คือมีบางเวลาที่เราไม่สามารถทำนายอนาคตได้

เพราะฉะนั้น เราอยากได้ความสัมพันธ์แบบพิเศษ ที่
> :red[1 Input ต้องโยงไปหา 1 Output เท่านั้น] จะมีกรณีที่ 1 Input ได้ Output ออกมาหลายตัวไม่ได้   
> และ :red[สมาชิกทุกตัวใน ***Domain*** ต้องเข้าร่วม] (Domain = เซตที่เป็นต้นเหตุ เช่น เวลา หรือ เซตของสัตว์)

เราเรียกความสัมพันธ์แบบพิเศษที่เข้าเงื่อนไขทั้งสองตัวนี้ว่า :violet[**Function, ฟังก์ชัน**]   

* :violet[**สัญลักษณ์ที่เกี่ยวกับฟังก์ชัน**]   

ถ้าเรามีฟังก์ชันตัวหนึ่ง ชื่อ :blue[f] ที่โยงสมาชิงของเซต :blue[A] เข้ากับเซต :blue[B] เราจะเขียนด้วยสัญลักษณ์   
:green[$\\; f:A \\mapsto B \\;$] อ่านว่า f เป็น Map จาก A ไป B (f is a map from A to B)   

''')