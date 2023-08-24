import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Functions and Derivatives', layout='centered')


st.header(':chart_with_upwards_trend: :violet[**Functions**] and Their :violet[**Derivatives**] :chart_with_upwards_trend:')
st.caption('Page นี้เป็นส่วนหนึ่งของคอร์ส :blue[สอวน. ฟิสิกส์ by Meerkat] สนใจติดต่อได้ที่ Facebook Page: :violet[**Physics Meerkat**]')

content = st.columns(2)
content[0].markdown(
    '''
:orange[**Contents**]
1. :blue[แนวคิดของฟังก์ชัน] 
2. :green[กราฟของฟังก์ชัน]
3. :orange[อัตราเร็วและความเร็วเฉลี่ย]
'''
)
with content[1]:
    add_vertical_space(2)
content[1].markdown(
    '''
4. :red[Limit และ ความเร็วชั่วขณะ]
5. :violet[The Derived Function (Derivatives)]
6. :blue[การหา Derivatives ของ Polynomials]
'''
)
st.divider()

topic_list = [':balloon: :blue[**แนวคิดของฟังก์ชัน**]',':balloon: :green[**กราฟของฟังก์ชัน**]',':balloon: :orange[**อัตราเร็วและความเร็วเฉลี่ย**]',
              ':balloon: :red[**Limit และ อัตราเร็วชั่วขณะ**]',':balloon: :violet[**The Derived function (Derivatives)**]',':balloon: :blue[**Derivatives ของ Polynomials**]']

topic=[]
for i in range(len(topic_list)):
    topic.append(st.expander(topic_list[i]))


#----Topic 1: แนวคิดของฟังก์ชัน----#
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


#----Topic 2: กราฟของฟังก์ชัน ----#
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
ที่เวลา :green[$t=0\\;s\\;$] รถคันนี้อยู่ห่างจากเริ่มต้นเป็นระยะ :green[$\\;S(0)=3(0)=0\\;m$]   
ที่เวลา :green[$t=1\\;s\\;$] รถคันนี้อยู่ห่างจากเริ่มต้นเป็นระยะ :green[$\\;S(1)=3(1)=3\\;m$]   
ที่เวลา :green[$t=2\\;s\\;$] รถคันนี้อยู่ห่างจากเริ่มต้นเป็นระยะ :green[$\\;S(2)=3(2)=6\\;m$]   
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

#----Topic 4: Limit และ ความเร็วชั่วขณะ----#
with topic[3]:
    st.markdown(
        '''
* :violet[**แนวคิดของ อัตราเร็วชั่วขณะ**] :balloon:   

ในหัวข้อที่แล้วเราหา :blue[อัตราเร็วเฉลี่ยบนช่วงเวลาหนึ่ง] คำถามถัดไปที่เราสนใจคือ
เราจะหา :violet[อัตราเร็วชั่วขณะที่เวลาหนึ่ง] ได้อย่างไร   
อัตราเร็วเฉลี่ยเราหาบน :blue[***ช่วงเวลา***] หนึ่งๆ นั่นแปลว่าเราต้องมีเวลาสองค่า เช่น หาอัตราเร็วเฉลี่ยในช่วง :green[$t=a$] ถึง :green[$t=b$] วินาที   
แต่อัตราเร็วชั่วขณะเราหา :blue[***ที่จุดๆเดียว***] เช่น หาอัตราเร็วชั่วขณะที่เวลา :green[$t=3$] วินาที เราสนใจว่า ที่ตรงนั้น ที่ตอนนั้น เรามีอัตราเร็วเท่าไหร่   
   
ไอเดียของการหาอัตราเร็วชั่วขณะคือ 
> ถ้าเราอยากได้:violet[อัตราเร็วชั่วขณะ]ที่เวลา :green[$t=3$] เราหา:violet[อัตราเร็วเฉลี่ย]ในช่วง :green[$t=3$] ถึงเวลา :green[$t=3+\\Delta t$] แล้วเราดูว่าเกิดอะไรขึ้นเมื่อ :green[$\\Delta t$ น้อยมากๆ]   
   
* :violet[**แนวคิดของ Limit**] :balloon:   

ปัญหาหนึ่งที่เราจะเจอเมื่อเราต้องการหาอัตราเร็วชั่วขณะคือ :blue[มันหาค่าไม่ได้]  
ตัวอย่างเช่น กำหนดให้รถคันหนึ่งมีระยะห่างจากบ้านเป็น :green[$S(t)=3t^2$] และเราต้องการหาอัตราเร็วชั่วขณะที่เวลา :green[$t=2\\;s$]    
เราทำได้โดยการหาอัตราเร็วเฉลี่ยในช่วง :green[$t=2$] ถึงเวลา :green[$t=2+\\Delta t$]   
$$
\\begin{align}
v_{t=2} &= \\frac{S(2+\\Delta t)-S(2)}{(2+\\Delta t) - 2} \\\\
&= \\frac{3(2+\\Delta t)^2 -3(2)^2}{\\Delta t} \\\\
&= \\frac{12+12\\Delta t +3\\Delta^2 t -12}{\\Delta t}
\\end{align}
$$   
จะเห็นว่า ถ้าเราแทน :green[$\\Delta t = 0$] ลงไปเลย เราจะได้ :green[$\\frac{0}{0}$] ซึ่งไม่นิยาม . . .(เราตัด $\\Delta t$ ไม่ได้ เพราะ $\\Delta t$ อาจจะมีค่าเป็น $0$ ได้)
เพราะฉะนั้น เราเฉลี่ยที่ตรงนั้น คือที่ :green[$t=2$] ตรงๆเลยไม่ได้   
แต่ถ้าเราบอกว่า :red[$\\Delta t \\not= 0 $] แต่ :red[$\\Delta t$] ใกล้ :red[$0$] มากๆ   
เราจะได้
$$
\\begin{align}
v_{t=2} &= \\frac{12\\Delta t + 3\\Delta^2 t}{\\Delta t} \\\\
&= 12+3\\Delta t . . .ตัดใด้เพราะ \\Delta t \\not = 0 \\\\
เมื่อ \\Delta t ใกล้\\;0\\;มากๆ . . . v_{t=2} &= 12
\\end{align}
$$   

ในตัวอย่างนี้ เราอยากจะเฉลี่ยที่ :green[$t=2$] ถึง :green[$t=2+\\Delta t$] แล้วดูว่าเกิดอะไรขึ้นเมื่อ :green[$\\Delta t$] น้อยมากๆ
แต่ปัญหาจะเกิดเมื่อ :green[$\\Delta t = 0$] มันจะหาค่าไม่ได้ เราเลยหลบไปบอกว่า :red[$\\Delta t \\not= 0 $] แต่ :red[$\\Delta t$] ใกล้ :red[$0$] มากๆ แทน   

การทำอะไรแบบนี้เราเรียกว่า :violet[การหา Limit ของฟังก์ชัน $S(t)=3t^2$ ที่ $t=2$]   
> โดยทั่วไป ถ้าเรามีฟังก์ชัน :blue[y=f(x)] แล้วเราต้องการดูว่าเกิดอะไรขึ้นกับฟังก์ชันนี้เมื่อ :blue[$x$] เข้าใกล้ :blue[$a$]   
> เราทำได้โดย :blue[การหา Limit] คือ เราดูว่าเกิดอะไรขึ้นเมื่อ :blue[$x$] เข้าใกล้ :blue[$a$] แต่ไม่สนว่าเกิดอะไรที่ :blue[$x=a$]   
> ถ้าค่าของฟังก์ชัน :blue[$y=f(x)$] :red[เข้าใกล้] :blue[$y=L$] เมื่อ :blue[$x$] :red[เข้าใกล้] :blue[$a$] เราเขียนเป็นสัญลักษณ์ดังนี้   
   
$$
🔸🔸🔸 \\lim_{x \\to a} f(x) = L 🔸🔸🔸
$$
'''
    )
    ex4_col = topic[3].columns([2,3])
    ex4_col[1].image('data/01_derivatives/illus_04.png',use_column_width=True)
    ex4_col[0].markdown(
        '''
ภาพด้านขวาคือฟังก์ชัน :blue[$y=x+1$] แต่ฟังก์ชันนี้ไม่นิยาม(มีรู)ที่ :blue[$x=2$]   
จากภาพ หากเราขยับ :green[$x \\to 2$] ไม่ว่าจากทางซ้ายหรือทางขวา จะเห็นว่าค่าของฟังก์ชัน :green[$y \\to 3$]   
เพราะฉะนั้นเราจะเขียนว่า 
$$
\\lim_{x \\to 2} x+1 = 3
$$   
'''
    )
    st.markdown(
        '''
คือ ถ้าเราขยับ :red[Input,$x$] ของฟังก์ชัน :blue[$y=x+1$] ให้เข้าใกล้ :blue[$x=2$] แล้ว :red[Output,$y$] จะเข้าใกล้ :blue[$y=3$]   
:orange[Note:] ที่ $x=2$ ฟังก์ชันไม่มีค่า เราก็สามารถหา Limit ได้เพราะ Limit สนใจว่า $y$ เข้าใกล้อะไร ไม่ได้สนใจว่า $y$ เท่ากับเท่าไหร่
เพราะเวลาเราหา $\\lim_{x \\to 2}$ เรามีเงื่อนไขว่า $x \\not = 2$
'''
    )


#---- Topic 5: The Derived Function (Derivatives)----#
with topic[4]:
    st.markdown(
        '''
ในหัวข้อที่แล้วเราเริ่มจาก ฟังก์ชันระยะทาง :blue[$S(t)$] จากนั้นเราหาอัตราเร็วชั่วขณะโดยการหาอัตราเร็วเฉลี่ยในช่วงสั้นๆรอบจุดที่จะหา   
จาก :green[$อัตราเร็ว = \\frac{ระยะทางที่เปลี่ยนไป}{เวลาที่ใช้เปลี่ยน}$] จะได้ว่า   
$$
\\begin{align}
🔸🔸🔸 v_{ชั่วขณะ} = \\lim_{\\Delta t \\to 0} \\frac{\\Delta S(t)}{\\Delta t} 🔸🔸🔸
\\end{align}
$$   
   
เรานิยามสัญลักษณ์ใหม่ขึ้นมา ดังนี้
$$
🔸🔸🔸\\frac{dS(t)}{dt} = \\lim_{\\Delta t \\to 0} \\frac{\\Delta S(t)}{\\Delta t} 🔸🔸🔸
$$   
   
สัญลักษณ์ :violet[$\\frac{dS(t)}{dt}$] อ่านว่า :violet[ดี-เอส-บาย-ดี-ที] หรือ :violet[อนุพันธ์ของฟังก์ชัน $S(t)$ เทียบ $t$, Derivative of $S(t)$ with respect to $t$]
> สัญลักษณ์ :red[$\\frac{dS(t)}{dt}$] มีความหมายคือ :blue[ค่าของฟังก์ชัน $S(t)$ ที่เปลี่ยนไป, $\\Delta S(t)$] ต่อ :blue[เวลาที่ใช้เปลียน,  $\\Delta t$] ใน Limit ที่ :red[$\\Delta t \\to 0$]   
   
ถ้ามีฟังก์ชัน :red[$y=f(x)$] เราสามารถหา :blue[Derivative, อนุพันธ์] ของฟังก์ชันได้ดังนี้   
1. ขยับ :red[Input] ไปนิดหน่อย. . . .เปลี่ยน :blue[$\\;f(x)\\;$] เป็น :blue[$\\;f(x+\\Delta x)$]   
2. ดูว่า :red[Output] เปลี่ยนไปเท่าไหร่. . . :blue[$y\\;$] เปลี่ยนเป็น :blue[$\\;y+\\Delta y$]   
3. หาสัดส่วน :blue[$\\frac{\\Delta y}{\\Delta x}$] แล้วดูว่าเกิดอะไรขึ้นเมื่อ :blue[$\\Delta x \\to 0$]    
4. จะได้ :blue[$\\frac{dy(x)}{dx} = \\lim_{\\Delta x \\to 0} \\frac{\\Delta y}{\\Delta x}$] ซึ่งจะบอกอัตราการเปลี่ยนแปลงของ :blue[$y=f(x)$] เมื่อเราขยับ :blue[$x$] ไปนิดหน่อย   
   
:orange[**Example:**] จงหา Derivative ของฟังก์ชัน :green[$S(t)=3t$]   
'''
    )
    example_05 = st.checkbox(':balloon:. . .ดูวิธีทำที่นี่',key='example_05')
    if example_05:
        st.markdown(
            '''
$$
\\begin{align}
S(t) &= 3t \\\\
S(t) + \\Delta S(t) &= 3(t+\\Delta t) \\\\
S(t) + \\Delta S(t) &= 3t + 3\\Delta t \\\\
\\Delta S(t) &= 3 \\Delta t . . .  from \\;v S(t)=3t \\\\
\\frac{\\Delta S(t)}{\\Delta t} &= 3 \\\\
\\lim_{\\Delta t \\to 0} \\frac{\\Delta S(t)}{\\Delta t} &= 3 \\\\
🔸🔸🔸 \\frac{dS(t)}{dt} &= 3 🔸🔸🔸
\\end{align}
$$   
เพราะฉะนั้น ถ้ามีรถที่เคลื่อนที่โดยมีฟังก์ชันระยะทางเป็น :green[$S(t)=3t$]   
จะได้ว่าอัตราเร็วชั่วขณะของรถนี้คือ :green[$\\frac{dS(t)}{dt}=3$]   
ก็คือรถคันนี้จะมีอัตราเร็วชั่วขณะเป็น :green[$\\;3\\;m/s\\;$] ตลอดเวลา :balloon:
'''
        )
    st.markdown(
        '''
:orange[**Example:**] จงหา Derivative ของฟังก์ชัน :green[$S(t)=3t^2$] 
'''
    )
    example_06 = st.checkbox(':balloon:. . .ดูวิธีทำที่นี่',key='example_06')
    if example_06:
        st.markdown(
            '''
$$
\\begin{align}
S(t) &= 3t^2 \\\\
S(t) + \\Delta S(t) &= 3(t+\\Delta t)^2 \\\\
S(t) + \\Delta S(t) &= 3(t^2 +2t\\Delta t + \\Delta^2 t) \\\\
S(t) + \\Delta S(t) &= 3t^2 + 6t\\Delta t + 3\\Delta^2 t \\\\
\\Delta S(t) &= 6t\\Delta t + 3\\Delta^2 t \\\\
\\frac{\\Delta S(t)}{\\Delta t} &= 6t + 3\\Delta t \\\\
\\lim_{\\Delta t \\to 0} \\frac{\\Delta S(t)}{\\Delta t} &= 6t \\\\
🔸🔸🔸 \\frac{dS(t)}{dt} &= 6t 🔸🔸🔸
\\end{align}
$$   
เพราะฉะนั้น ถ้ารถเคลื่อนที่โดยมีฟังก์ชันระยะทางเป็น :green[$S(t)=3t^2$]   
จะมีอัตราเร็วชั่วขณะเป็น :green[$\\frac{dS(t)}{dt}=6t$] นั่นคือ   
ที่เวลา :green[$t=0$] รถมีอัตราเร็วชั่วขณะเป็น :green[$\\frac{dS(t)}{dt}|_{t=0}=6(0)=0\\;m/s$]   
ที่เวลา :green[$t=1$] รถมีอัตราเร็วชั่วขณะเป็น :green[$\\frac{dS(t)}{dt}|_{t=1}=6(1)=6\\;m/s$]   
ที่เวลา :green[$t=2$] รถมีอัตราเร็วชั่วขณะเป็น :green[$\\frac{dS(t)}{dt}|_{t=2}=6(2)=12\\;m/s$]   
ที่เวลา :green[$t=3$] รถมีอัตราเร็วชั่วขณะเป็น :green[$\\frac{dS(t)}{dt}|_{t=3}=6(3)=18\\;m/s$]  
   
ก็คือ :blue[Derivative ของฟังก์ชันระยะทาง] :blue[$S(t)=3t^2$] จะเป็นฟังก์ชันอีกตัวหนึ่ง คือ   
:blue[ฟังก์ชันของอัตราเร็ว] :blue[$v(t)=6t$] โดยฟังก์ชันตัวนี้จะบอกว่า ที่เวลาต่างๆ รถคันนี้จะมี อัตราเร็วชั่วขณะ เป็นเท่าไหร่   
เพราะฉะนั้น ถ้าเราหาอนุพันธ์ของฟังก์ชันระยะทาง เราจะได้ฟังก์ชันอัตราเร็ว   
$$
🔸🔸🔸 \\frac{dS(t)}{dt}=v(t) 🔸🔸🔸
$$   
เราเรียก :blue[การหาอนุพันธ์] ว่า :blue[Differentiation] หรือแบบย่อว่า :blue[Diff] เพราะฉะนั้น :violet[**ดิฟระยะทางได้อัตราเร็ว**]  
สอดคล้องกับความหมายทางฟิสิกส์ที่ว่า :violet[**อัตราเร็ว คือ อัตราการเปลี่ยนแปลงระยะทาง**] นั่นเอง

'''
        )



#---- Topic 6: Derivatives of Polynomials----#
with topic[5]:
    st.markdown(
        '''
hello
'''
    )

