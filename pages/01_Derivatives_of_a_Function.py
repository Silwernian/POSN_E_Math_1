import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Functions and Derivatives', layout='centered')


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

topic_list = [':blue[**แนวคิดของฟังก์ชัน**]',':green[**กราฟของฟังก์ชัน**]',':orange[**อัตราเร็วและความเร็วเฉลี่ย**]',
              ':red[**Limit และ อัตราเร็วชั่วขณะ**]',':violet[**The Derived function (Derivatives)**]',':blue[**Derivatives ของ Polynomials**]']

topic=[]
for i in range(len(topic_list)):
    topic.append(st.expander(topic_list[i]))
    topic[i].write('remove later . . .')


with topic[0]:
    st.markdown(
        '''
* :violet[**Set**] :pushpin:      

ในคณิตศาสตร์ เวลาที่เราเอา Objects มากองรวมๆกัน เราเรียกทั้งกองนั้นว่า :blue[**Set**] เช่น    
$A=\{ หมา, แมว, เป็ด, ไก่, . . . \}=\{ x| x = สัตว์\} $ อ่านว่า :green[A คือเซตของ $x$ เมื่อ $x$ คือสัตว์]   
$B=\{ ส้ม, แดง, เขียว, น้ำเงิน, . . .\}=\{y|y = สี \} $ อ่านว่า :green[B คือเซตของ $y$ เมื่อ $y$ คือสี]   
เซตบางตัวที่เจอบ่อย ควรรู้จักชื่อไว้ . . .   
:blue[**Natural Number**] : $\\N= \{ 1,2,3,4,5,6,... \}$    
:blue[**Interger**]: $\\Z= \{ ...,-3,-2,-1,0,+1,+2,+3,...\}$    
:blue[**Real Number**]: $\\R= \{ จำนวนจริง \}$    

* :violet[**Relations**] :pushpin:      
   
เมื่อเรามี Set แล้ว สิ่งถัดมาที่เราอาจจะอยากได้คือ ***อะไรสักอย่างที่โยงเซตสองเซตเข้าด้วยกัน*** ในคณิตศาสตร์เราเรียกสิ่งนั้นว่า :blue[**Relation, ความสัมพันธ์**]   
เช่น เราอาจจะสร้าง Relation ระหว่าง Set A กับ B ได้โดยนิยาม Relation จาก A ไป B ให้เป็น :orange[โยงสัตว์เข้ากับสีของมัน]   
หมา อาจมีสี ขาว ดำ เทา เพราะฉะนั้น จะได้ :green[$หมา \mapsto ขาว, ดำ, เทา$]   
แมว อาจมี แมวขาว แมวดำ แมวส้ม แมวเทา จะได้ :green[$แมว \mapsto ขาว, ดำ, ส้ม, เทา$]    
''')
    function_col = topic[0].columns([3,2])
    function_col[0].markdown(
        '''
* :violet[**Functions**] :pushpin:      
   
จะเห็นว่า Relation ก็มีประโยชน์แล้ว มันใช้โยงสองสิ่งเข้าด้วยกัน แต่ว่าในฟิสิกส์(วิทยาศาสตร์) ถ้าใช้ Relation ไปเลยมันอาจจะเกิดปัญหาแปลกๆแบบนี้   
สมมุติเราอยากทำนายว่า ที่เวลาต่างๆลูกบอลอยู่ที่ไหน เราให้ :green[$t = \{ 1,2,3,...\}$] แทนเวลาต่างๆ ที่เราอยากทำนาย และเราให้
:green[$ x = \{ ...,-2,-1,0,1,2,... \}$] แทนตำแหน่งต่างๆที่เป็นไปได้ เพราะฉะนั้น เราควรสร้างความสัมพันธ์ที่โยง :green[$\\;t$, เวลา] เข้ากับ :green[$\\;x$, ตำแหน่ง]   
แต่ว่าถ้าเราอยากทำนายอนาคต มันควรมีข้อจำกัดดังนี้
1. ถ้าเราเลือกเวลามา 1 ตัว เราควรได้ตำแหน่งแค่ตำแหน่งเดียว :orange[$1\\;input \mapsto 1\\;output$] ไม่งั้นมันจะเกิดกรณีที่เราเลือกเวลามาหนึ่งตัว แต่ได้หลายตำแหน่ง ก็คือเราทำนายอนาคตไม่ได้นั่นเอง
2. เซต :green[$\\;t\\;$] แทนเวลาที่เราอยากทำนาย เพราะฉะนั้น :orange[ทุกตัวใน $\\;t\\;$ ควรเข้าร่วมกับ Relation นี้] ไม่งั้นจะกลายเป้นว่ามีบางเวลาที่ไม่ได้เข้าร่วม คือมีบางเวลาที่เราไม่สามารถทำนายอนาคตได้

เพราะฉะนั้น เราอยากได้ความสัมพันธ์แบบพิเศษ ที่
> :red[1 Input ต้องโยงไปหา 1 Output เท่านั้น] จะมีกรณีที่ 1 Input ได้ Output ออกมาหลายตัวไม่ได้   
> และ :red[สมาชิกทุกตัวใน ***Domain*** ต้องเข้าร่วม] (Domain = เซตที่เป็นต้นเหตุ เช่น เวลา หรือ เซตของสัตว์)

เราเรียกความสัมพันธ์แบบพิเศษที่เข้าเงื่อนไขทั้งสองตัวนี้ว่า :blue[**Function, ฟังก์ชัน**]   


'''
    )
    function_col[1].image('data/01_derivatives/illus_01.png',use_column_width=True)
    st.markdown(
        '''
* :violet[**สัญลักษณ์ที่เกี่ยวกับฟังก์ชัน**] :pushpin:   

ถ้าเรามีฟังก์ชันตัวหนึ่ง ชื่อ :blue[f] ที่โยงสมาชิงของเซต :blue[A] เข้ากับเซต :blue[B] เราจะเขียนด้วยสัญลักษณ์   
:green[$\\; f:A \\mapsto B \\;$] อ่านว่า f เป็น Map จาก A ไป B (f is a map from A to B)    
ปกติเรามักจะตั้งชื่อฟังก์ชันว่า :green[**f, g, h**] และเราเอาตัวแปร :green[**Output**] ใส่ในวงเล็บด้านหลัง   
เช่น :green[$\\;  y=f(x)\\;$] หมายความว่าเรามีฟังก์ชันตัวหนึ่ง ชื่อ :green[**f**] เราเอา :green[**x**] มาใส่ แล้วเราจะได้ :green[**y**] ออกมา  
   
อีกวิธีหนึ่งที่เราใช้บ่อยในการเขียนแสดงฟังก์ชันคือ :green[เขียนแสดงกฏการโยงสมาชิก] ออกมาตรงๆเลย   
อย่างเช่น :blue[$\\; f(x)=x^2 + 1\\;$] แปลว่า ฟังก์ชันนี้ชื่อ :green[**f**] และถ้าเรายัด :green[**$x$**] เข้าไป มันจะให้ :green[**$x^2 + 1$**] ออกมา   
ตัวอย่าง ให้ :blue[$\\; f(x)=x^2 + 1 \\;$]   จะได้ว่า 
:green[$\\; f(1)=(1)^2 + 1 = 2 \\;$]   
:green[$\\; f(2)=(2)^2 + 1 = 5 \\;$]   
:green[$\\; f(3)=(3)^2 + 1 = 10 \\;$]   
คิดว่า :blue[Function] ทำหน้าที่เป็น Blueprint ก็ได้ ตัวฟังก์ชันจะบอกว่า ถ้าเรายัดตัวนี้เข้ามา มันจะให้อะไรออกมา
> :blue[Function] ไม่ใช่ Input หรือ Output แต่ :blue[Function] คือสิ่งที่โยงทั้งสองเข้าด้วยกัน   
> นาย A :blue[เป็นพ่อของ] นาย B คำว่า :blue[เป็นพ่อของ] ไม่ใช่ทั้งนาย A หรือนาย B แต่มันคืออะไรสักอย่างที่โยงทั้งสองเข้าด้วยกัน  
'''
    )
    example1 = st.checkbox(':orange[ตัวอย่างโจทย์การแทนค่าฟังก์ชัน]')
    if example1:
        st.markdown(
            '''
กำหนดให้ :blue[$f(x)=3x^2 +2x+1$] จงหาค่าของ :blue[$f(0),\\;f(1),\\;f(x+\\Delta x)$]   
$f(0)=3(0)^2+2(0)+1 = 1$   
$f(1)=3(1)^2+2(1)+1 = 6$   
$$
\\begin{align}
f(x+\\Delta x) &= 3(x+\\Delta x)^2+2(x+\\Delta x)+1 \\\\
&= 3\{x^2 +2x\\Delta x + \\Delta^2 x  \} +2x +2\\Delta x +1 \\\\
&= 3x^2 +6x\\Delta x + 3 \\Delta^2 x   +2x +2\\Delta x +1 \\\\
f(x+\\Delta x) &=  3x^2+2x+1 + (6x+2)\\Delta x +3\\Delta^2 x 
\\end{align}
$$
'''
        )

#----Topic 1: กราฟของฟังก์ชัน ----#
with topic[1]:
    st.markdown(
        '''
ตอนนี้เราน่าจะพอรู้จัก :violet[Function] กันมากขึ้นแล้ว  . . . แต่ว่าเวลาเขียน :blue[$\\; f(x)=x+1\\;$] เราไม่เห็นภาพว่านี่คืออะไร
ในฟิสิกส์เราอยากได้วิธีมองสิ่งต่างๆเป็นภาพ จะได้บอกได้คร่าวๆว่ามันเกิดอะไรขึ้นแบบหยาบๆ หนึ่งในวิธีที่เราใช้ :blue[มองฟังก์ชันออกมาเป็นภาพ] ก็คือ :blue[การพลอตกราฟ]
'''
    )
    top1_col = st.columns([1,1])

    top1_col[1].image('data/01_derivatives/illus_02.png')
    top1_col[0].markdown(
        '''
* :violet[**ระบบพิกัด, Coordinate System**] :pushpin:   

ในการจะวาดภาพ สิ่งที่แรกที่เราต้องมีก็คือกระดาษ :violet[ระบบพิกัด, Coordinate System] ก็คือกระดาษสำหรับวาดกราฟลงไป เราตั้งแกนขึ้นมาสองแกนที่ตั้งฉากกัน
:blue[แกน$\\;x\\;$ และแกน $\\;y$] เราจะได้ตารางเต็มหน้ากระดาษ . . . จากนั้นเวลาเราจิ้มนิ้วลงไปที่แต่ละจุด เราจะได้ตัวเลขออกมาสองตัว :violet[$(x,y)$]
อย่างเช่น :violet[จุดสีม่วง, A] เราจิ้มนิ้วลงไปที่จุดนั้น จากนั้นเราลากเส้นตั้งฉากจากจุดนั้นไปหาแกน $\\;x\\;$ และแกน $\\;y\\;$ เส้นนี้ไปตัดแกนที่เลขอะไร เราก็เอามาใส่
จะได้ :violet[A แทนด้วย (2,1)] แปลว่าจุด :violet[A] ลากเส้นมาตัดกับแกน :blue[$\\;x\\;$] ที่ :blue[$\\; x=2\\;$] และลากเส้นมาตัดกับแกน :blue[$\\;y\\;$] ที่ :blue[$\\; y=1\\;$]
'''
    )

    st.markdown(
        '''
* :violet[**กราฟของฟังก์ชัน**] :pushpin: 

การพลอตกราฟของฟังก์ชันเราทำได้โดย
> เลือก Input มาใส่ฟังก์ชันทีละตัว แล้วดูว่าได้ Output อะไร จากนั้น Plot 1 จุด   

เช่น ถ่าเราสนใจฟังก์ชัน :blue[$\\; f(x)=x+1\\;$] จะได้ตารางหน้าตาแบบนี้ออกมา   
|:blue[x]|:blue[0]|:blue[1]|:blue[2]|:blue[3]|:blue[4]|:blue[5]|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|:green[y=f(x)]|:green[1]|:green[2]|:green[3]|:green[4]|:green[5]|:green[6]|
|จุดที่ Plot คือ (:blue[x],:green[y])|(:blue[0],:green[1])|(:blue[1],:green[2])|(:blue[2],:green[3])|(:blue[3],:green[4])|(:blue[4],:green[5])|(:blue[5],:green[6])|
'''
    )

    st.image('data/01_derivatives/illus_03.png',use_column_width=True)
    st.markdown(
        '''
:orange[**Example 02:**]   
จงพลอตกราฟของฟังก์ชันต่อไปนี้
1. :green[$\\; y=2x-1 \\;$]
2. :green[$\\; y=x^2 -2 \\;$]
3. :green[$\\; y=\\sin(x) \\;$]
'''
    )
    ex_2_soln = st.checkbox(':red[ดูเฉลยที่นี่. . .:balloon: ]')
    if ex_2_soln:
        ex02_col = topic[1].columns([1,1])
        ex02_col[0].markdown(':blue[กราฟ. . . $y=2x-1$]')
        x1 = np.linspace(-1.5,2.5,50)
        y = 2*x1-1
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=x1,y=y,line_color='aqua', line_width=5))
        fig1.update_xaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        fig1.update_yaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        ex02_col[0].plotly_chart(fig1,use_container_width=True)

        ex02_col[1].markdown(':blue[กราฟ. . . $y=x^2-2$]')
        x2 = np.linspace(-3.5,3.5,50)
        y2 = x2**2-2
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=x2,y=y2,line_color='aqua', line_width=5))
        fig2.update_xaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        fig2.update_yaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        ex02_col[1].plotly_chart(fig2,use_container_width=True)

        st.markdown(':blue[กราฟ. . . $y=\\sin x$]')
        x3 = np.linspace(-1.5*np.pi,1.5*np.pi,50)
        y3 = np.sin(x3)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=x3,y=y3,line_color='aqua', line_width=5))
        fig3.update_xaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        fig3.update_yaxes(showgrid=True, zeroline=True, zerolinewidth=0.3, zerolinecolor='yellow')
        st.plotly_chart(fig3,use_container_width=True)

#---- Topic 3: อัตราเร็วและความเร็วเฉลี่ย----#
with topic[2]:
    st.markdown(
        '''
ในการศึกษาการเคลื่อนที่ของวัตถุ เราสนใจว่า ที่เวลาหนึ่งๆวัตถุเคลื่อนที่ไปได้เท่าไหร่ ใกลจากจุดอ้างอิงเท่าไหร่
ก็คือ เราเขียนฟังก์ชัน :orange[ระยะห่างจากจุดอ้างอิง] ที่เวลาใดๆ ออกมา
$$
 S=S(t) \\;. . . \\;อ่านว่า \\;S\\; เป็นฟังก์ชันของ \\;t 
$$   

ตัวอย่างเช่น รถคันหนึ่งมีระยะจากจุดเริ่มต้นเป็น :blue[$S(t)=3t\\;m$] แปลว่า   
ที่เวลา :green[$t=0\\;s\\;$] รถคันนี้อยู่ห่างจาดเริ่มต้นเป็นระยะ :green[$\\;S(0)=3(0)=0\\;m$]   
ที่เวลา :green[$t=1\\;s\\;$] รถคันนี้อยู่ห่างจาดเริ่มต้นเป็นระยะ :green[$\\;S(1)=3(1)=3\\;m$]   
ที่เวลา :green[$t=2\\;s\\;$] รถคันนี้อยู่ห่างจาดเริ่มต้นเป็นระยะ :green[$\\;S(2)=3(2)=6\\;m$]   
. . .   
:red[**Definition:**] 
$$
🔸🔸🔸อัตราเร็วเฉลี่ย=\\frac{ระยะทางที่เคลื่อนที่ได้}{เวลาที่ใช้}🔸🔸🔸
$$   
เพราะฉะนั้น ถ้าเราอยากหา :blue[อัตราเร็วเฉลี่ย; Average Velocity,$\\;v_{av}\\;$] ของวัตถุ เราต้องบอกก่อนว่า :blue[เฉลี่ยจากเวลาเท่าไหร่ถึงเท่าไหร่]   
สมมุติมีรถคันหนึ่งเคลื่อนที่โดยมีระยะจากจุดเริ่มต้นที่เวลาใดๆเป็น :blue[$S(t)=3t\\;m$]   
และเราอยากหาอัตราเร็วเฉลี่ยตั้งแต่เวลา :blue[$\\;t=0\\;s\\;$] ถึง :blue[$\\;t=3\\;s\\;$] จะได้ 
$$
อัตราเร็วเฉลี่ยในช่วง\\;0\\;ถึง\\;3\\;วินาที,\\; v_{av} = \\frac{ระยะทางที่ได้ในช่วง\\;0\\;ถึง\\;3\\;วินาที}{เวลาที่ใช้ในช่วง\\;0\\;ถึง\\;3\\;วินาที}
$$
ที่เวลา :green[0] วินาที รถเคลื่อนที่ได้ระยะทาง :green[$\\;S(0)=3(0)=0\\;m\\;$]   
ที่เวลา :green[3] วินาที รถเคลื่อนที่ได้ระยะทาง :green[$\\;S(3)=3(3)=9\\;m\\;$]   
เพราะฉะนั้น ในช่วงเวลา :blue[0] ถึง :blue[3] วินาที รถเคลื่อนที่ได้ระยะทาง :blue[$$S(3)-S(0)=9-0=9\\;m$$]   
เวลาที่เดินไปในช่วงเวลา :blue[0] ถึง :blue[3] วินาที คือ :blue[$\\; \\Delta t = 3\\;s$]   
เพราะฉะนั้น อัตราเร็วเฉลี่ยในช่วง :blue[0] ถึง :blue[3] วินาที คือ :blue[$v_{av}=\\frac{9\\;m}{3\\;s}=3\\;m/s$]   
   
โดยทั่วไป ถ้าเรามี :blue[ฟังก์ชันระยะทาง,$\\;S=S(t)$] มาให้ และเราต้องการหา :blue[อัตราเร็วเฉลี่ยในช่วง $\\;t \\in [t_1,t_2]$]
เราสามารถหาได้โดย
$$
\\begin{align}
v_{av} &= \\frac{S(t_2)-S(t_1)}{t_2 - t_1} \\\\
\\end{align}
$$
หรือ :violet[$\\;v_{av}=\\frac{\\Delta S(t)}{\\Delta t}$]. . . อ่านว่า :blue["ระยะทางที่เปลี่ยนไป ส่วน เวลาที่ใช้"]   
   
:orange[**Example:**]   
นาย A เคลื่อนที่โดยมีระยะห่างจากบ้านที่เวลาใดๆเป็น :blue[$\\;S_A(t)=5t+3\\;m$]   
นาย B เคลื่อนที่โดยมีระยะห่างจากบ้านที่เวลาใดๆเป็น :blue[$\\;S_B(t)=0.5t^2\\;m$]   
> :orange[Q1:] ที่เวลา $\\;t=4\\;s\\;$ ใครอยู่ห่างจากบ้านมากกว่ากัน   
> :orange[Q2:] ที่เวลาเท่าไหร่ ทั้งสองถึงจะอยู่ห่างจากบ้านเป็นระยะเท่ากัน (วาดกราฟ $\\;S(t)\\;$ของทั้งสองด้วย)     
> :orange[Q3:] ในช่วง $\\;t=10\\;s\\;$ ถึง $\\;t=20\\;s\\;$ ใครมีอัตราเร็วเฉลี่ยมากกว่ากัน 
'''
    )
    ex03_soln = st.checkbox(':blue[ดูเฉลยที่นี่ . . .:balloon:]')
    if ex03_soln:
        st.markdown(
            '''
:orange[**Question 1:**]   
ที่เวลา $\\;t=4\\;s\\;$ นาย A อยู่ห่างจากบ้านเป็นระยะ $\\; S_A(4)=5(4)+3=23\\;m\\;$   
ที่เวลา $\\;t=4\\;s\\;$ นาย B อยู่ห่างจากบ้านเป็นระยะ $\\; S_B(4)=0.5(4)^2=8\\;m\\;$   
เพราะฉะนั้น :green[ที่เวลา $\\;t=4\\;s\\;$ นาย A อยู่ห่างจากบ้านมากกว่า] :balloon:''')
        ex03_col=topic[2].columns([1,1])
        ex03_col[0].markdown(
'''
:orange[**Question 2:**]   
ให้ :blue[$\\;t_x\\;$] แทนเวลาที่ทั้งสองอยู่ห่างจากบ้านเป็นระยะเท่ากัน จะได้ว่า
$$
\\begin{align}
S_A(t_x) &= S_B(t_x) \\\\ 
5(t_x)+3 &= 0.5(t_x)^2 \\\\
5t_x + 3 &= \\frac{1}{2}t_x^2 \\\\
t_x^2 - 10t_x - 6 &= 0 
\\end{align}
$$
จะแก้ได้ $t_x = 10.6\\;s,\\; -0.568 \\;s$   
เพราะฉะนั้น เวลาที่ทั้งสองห่างจากบ้านเป็นระยะเท่ากันคือ :green[$t=10.6\\;s$] :balloon:   
จะเห็นว่ากราฟ $S(t)$ ของทั้งสองตัดกันที่ตรงนี้พอดี
'''
        )
        ex03_col[1].image('data/01_derivatives/ex_03_01.png',use_column_width=True)
        st.markdown(
            '''
:orange[**Question 3:**]   
$$
\\begin{align}
v_A &= \\frac{S_A(20)-S_A(10)}{20\\;s-10\\;s} \\\\
&= \\frac{[5(20)+3]-[5(10)+3]}{10\\;s} \\\\
&= \\frac{50\\;m}{10\\;s} \\\\
🔹🔹v_A&= 5\\;m/s🔹🔹
\\end{align}
$$

$$
\\begin{align}
v_B &= \\frac{S_B(20)-S_B(10)}{20\\;s-10\\;s} \\\\
&= \\frac{[0.5(20)^2]-[0.5(10)^2]}{10\\;s} \\\\
&= \\frac{150\\;m}{10\\;s} \\\\
🔹🔹v_B&= 15\\;m/s 🔹🔹
\\end{align}
$$

เพราะฉะนั้น :green[ในช่วง $t \\in [10\\;s,20\\;s]$ B มีอัตราเร็วเฉลี่ยมากกว่า A] :balloon:
'''
        )