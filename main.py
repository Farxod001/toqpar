import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.core.window import Window


x=0
top='yuq'

Builder.load_string('''

<PageLayout>:
	

	border: 10


	GridLayout:
	    cols: 2
	    rows: 1
	    
	    GridLayout:
	        cols: 1
	        rows: 14
	    	Label:    
	        	id: yul4
	        	text: "4.yul="            
	        	bold: True            	
	    	Label:    
	        	id: yul3
	        	text: "3.yul="            
	        	bold: True            
	    	Label:    
	        	id: yul5
	        	text: "5.yul="            
	        	bold: True            	
	    	Label:    
	        	id: yul7
	        	text: "7.yul="            
	        	bold: True  
	    	Label:    
	        	id: yul9
	        	text: "9.yul="            
	        	bold: True            
	    	Label:    
	        	id: yul11
	        	text: "11.yul="            
	        	bold: True            
	    	Label:    
	        	id: yul13
	        	text: "13.yul="            
	        	bold: True  	
	    	Label:    
	        	id: sef1
	        	text: "1.sef="            
	        	bold: True  
	    	Label:    
	        	id: sef2
	        	text: "2.sef="            
	        	bold: True
	    	Label:    
	        	id: sef3
	        	text: "3.sef="            
	        	bold: True
	    	Label:    
	        	id: sef4
	        	text: "4.sef="            
	        	bold: True
	    	Label:    
	        	id: sef5
	        	text: "5.sef="            
	        	bold: True
	    	Label:    
	        	id: sef6
	        	text: "6.sef="            
	        	bold: True
	    	Label:    
	        	id: summ
	        	text: "jami="            
	        	bold: True

	    GridLayout:
	        cols: 1
	        rows: 14
	        size_hint: .2,1
	    	Label:    
	        	id: yu4
	        	text: ""            
	        	bold: True            	
	    	Label:    
	        	id: yu3
	        	text: ""            
	        	bold: True            
	    	Label:    
	        	id: yu5
	        	text: ""            
	        	bold: True            	
	    	Label:    
	        	id: yu7
	        	text: ""            
	        	bold: True  
	    	Label:    
	        	id: yu9
	        	text: ""            
	        	bold: True            
	    	Label:    
	        	id: yu11
	        	text: ""            
	        	bold: True            
	    	Label:    
	        	id: yu13
	        	text: ""            
	        	bold: True  	
	    	Label:    
	        	id: se1
	        	text: ""            
	        	bold: True  
	    	Label:    
	        	id: se2
	        	text: ""            
	        	bold: True
	    	Label:    
	        	id: se3
	        	text: ""            
	        	bold: True
	    	Label:    
	        	id: se4
	        	text: ""            
	        	bold: True
	    	Label:    
	        	id: se5
	        	text: ""            
	        	bold: True
	    	Label:    
	        	id: se6
	        	text: ""            
	        	bold: True
	    	Label:    

	        	text: ""            
	        	bold: True

	BoxLayout:
		orientation: "vertical"


    	GridLayout:
        	cols: 7
        	rows: 2
			size_hint: 1,.2
        	Button:

                id: i0
            	text: "y4" 
            	on_press: root.k0()      	

        	Button:
            	id: i1
            	text: "y3"
            	
            	on_press: root.k1()
        	Button:
            	id: i2
            	text: "y5"
            	on_press: root.k2()
        	Button:
            	id: i3
            	text: "y7"
            	on_press: root.k3()
        	Button:
            	id: i4
            	text: "y9"
            	on_press: root.k4()
        	Button:
            	id: i5
            	text: "y11"
            	on_press: root.k5()
        	Button:
            	id: i6
            	text: "y13"
            	on_press: root.k6()
        	Button:
            	id: i7
            	text: "s1"
            	on_press: root.k7()
        	Button:
            	id: i8
            	text: "s2"
            	on_press: root.k8()
        	Button:
            	id: i9
            	text: "s3"
            	on_press: root.k9()
        	Button:
            	id: i10
            	text: "s4"
            	on_press: root.k10()
        	Button:
            	id: i11
            	text: "s5"
            	on_press: root.k11()
        	Button:
            	id: i12
            	text: "s6"
            	on_press: root.k12()
        	Label:

        		id: kur
            	text: "yuq"




		ScrollView:
			do_scroll_x: False
			do_scroll_y: True




			GridLayout:
				cols:5 
				rows: 18
				size_hint_y: None
				height: 1500
				Button:
					id: b1
					text: '91'
					on_press: root.v1()
				Button:
					id: b2
					text: '92'
					on_press: root.v2()
				Button:
					id: b3
					text: '93'
					on_press: root.v3()
				Button:
					id: b4
					text: '94'
					on_press: root.v4()
				Button:
					id: b5
					text: '95'
					on_press: root.v5()
				Button:
					id: b6
					text: '96'
					on_press: root.v6()
				Button:
					id: b7
					text: '97'
					on_press: root.v7()
				Button:
					id: b8
					text: '98'
					on_press: root.v8()
				Button:
					id: b9
					text: '99'
					on_press: root.v9()
				Button:
					id: b10
					text: '100'
					on_press: root.v10()
				Button:
					id: b11
					text: '101'
					on_press: root.v11()
				Button:
					id: b12
					text: '102'
					on_press: root.v12()
				Button:
					id: b13
					text: '103'
					on_press: root.v13()
				Button:
					id: b14
					text: '104'
					on_press: root.v14()
				Button:
					id: b15
					text: '105'
					on_press: root.v15()
				Button:
					id: b16
					text: '106'
					on_press: root.v16()
				Button:
					id: b17
					text: '107'
					on_press: root.v17()
				Button:
					id: b18
					text: '108'
					on_press: root.v18()
				Button:
					id: b19
					text: '109'
					on_press: root.v19()
				Button:
					id: b20
					text: '110'
					on_press: root.v20()
				Button:
					id: b21
					text: '111'
					on_press: root.v21()
				Button:
					id: b22
					text: '112'
					on_press: root.v22()
				Button:
					id: b23
					text: '113'
					on_press: root.v23()
				Button:
					id: b24
					text: '114'
					on_press: root.v24()
				Button:
					id: b25
					text: '115'
					on_press: root.v25()
				Button:
					id: b26
					text: '116'
					on_press: root.v26()
				Button:
					id: b27
					text: '117'
					on_press: root.v27()
				Button:
					id: b28
					text: '118'
					on_press: root.v28()
				Button:
					id: b29
					text: '119'
					on_press: root.v29()
				Button:
					id: b30
					text: '120'
					on_press: root.v30()
				Button:
					id: b31
					text: '121'
					on_press: root.v31()
				Button:
					id: b32
					text: '122'
					on_press: root.v32()
				Button:
					id: b33
					text: '123'
					on_press: root.v33()
				Button:
					id: b34
					text: '124'
					on_press: root.v34()
				Button:
					id: b35
					text: '125'
					on_press: root.v35()
				Button:
					id: b36
					text: '126'
					on_press: root.v36()
				Button:
					id: b37
					text: '127'
					on_press: root.v37()
				Button:
					id: b38
					text: '128'
					on_press: root.v38()
				Button:
					id: b39
					text: '129'
					on_press: root.v39()
				Button:
					id: b40
					text: '130'
					on_press: root.v40()
				Button:
					id: b41
					text: '131'
					on_press: root.v41()
				Button:
					id: b42
					text: '132'
					on_press: root.v42()
				Button:
					id: b43
					text: '133'
					on_press: root.v43()
				Button:
					id: b44
					text: '134'
					on_press: root.v44()
				Button:
					id: b45
					text: '135'
					on_press: root.v45()
				Button:
					id: b46
					text: '136'
					on_press: root.v46()
				Button:
					id: b47
					text: '137'
					on_press: root.v47()
				Button:
					id: b48
					text: '138'
					on_press: root.v48()
				Button:
					id: b49
					text: '139'
					on_press: root.v49()
				Button:
					id: b50
					text: '140'
					on_press: root.v50()
				Button:
					id: b51
					text: '141'
					on_press: root.v51()
				Button:
					id: b52
					text: '142'
					on_press: root.v52()
				Button:
					id: b53
					text: '143'
					on_press: root.v53()
				Button:
					id: b54
					text: '144'
					on_press: root.v54()
				Button:
					id: b55
					text: '145'
					on_press: root.v55()
				Button:
					id: b56
					text: '146'
					on_press: root.v56()
				Button:
					id: b57
					text: '147'
					on_press: root.v57()
				Button:
					id: b58
					text: '148'
					on_press: root.v58()
				Button:
					id: b59
					text: '149'
					on_press: root.v59()
				Button:
					id: b60
					text: '150'
					on_press: root.v60()
				Button:
					id: b61
					text: '151'
					on_press: root.v61()
				Button:
					id: b62
					text: '152'
					on_press: root.v62()
				Button:
					id: b63
					text: '153'
					on_press: root.v63()
				Button:
					id: b64
					text: '154'
					on_press: root.v64()
				Button:
					id: b65
					text: '155'
					on_press: root.v65()
				Button:
					id: b66
					text: '156'
					on_press: root.v66()
				Button:
					id: b67
					text: '157'
					on_press: root.v67()
				Button:
					id: b68
					text: '158'
					on_press: root.v68()
				Button:
					id: b69
					text: '159'
					on_press: root.v69()
				Button:
					id: b70
					text: '160'
					on_press: root.v70()
				Button:
					id: b71
					text: '161'
					on_press: root.v71()
				Button:
					id: b72
					text: '162'
					on_press: root.v72()
				Button:
					id: b73
					text: '163'
					on_press: root.v73()
				Button:
					id: b74
					text: '164'
					on_press: root.v74()
				Button:
					id: b75
					text: '165'
					on_press: root.v75()
				Button:
					id: b76
					text: '166'
					on_press: root.v76()
				Button:
					id: b77
					text: '167'
					on_press: root.v77()
				Button:
					id: b78
					text: '168'
					on_press: root.v78()
				Button:
					id: b79
					text: '169'
					on_press: root.v79()
				Button:
					id: b80
					text: '170'
					on_press: root.v80()
				Button:
					id: b81
					text: '171'
					on_press: root.v81()
				Button:
					id: b82
					text: '172'
					on_press: root.v82()
				Button:
					id: b83
					text: '173'
					on_press: root.v83()
				Button:
					id: b84
					text: '174'
					on_press: root.v84()
				Button:
					id: b85
					text: '175'
					on_press: root.v85()
				Button:
					id: b86
					text: '176'
					on_press: root.v86()
				Button:
					id: b87
					text: '177'
					on_press: root.v87()
				Button:
					id: b88
					text: '178'
					on_press: root.v88()
				Button:
					id: b89
					text: '179'
					on_press: root.v89()
				Button:
					id: b90
					text: '180'
					on_press: root.v90()





	''')


w4=0
w3=0
w5=0
w7=0
w9=0
w11=0
w13=0
e1=0
e2=0
e3=0
e4=0
e5=0
e6=0
j=0
class PageLayout(PageLayout):


	def __init__(self, **kwargs):
		super(PageLayout, self).__init__(**kwargs)


	def k0(self):
		global top
		top=self.ids.i0.text
		self.ids.kur.text=self.ids.i0.text
	def k1(self):
		global top
		top=self.ids.i1.text
		self.ids.kur.text=self.ids.i1.text
	def k2(self):
		global top
		top=self.ids.i2.text
		self.ids.kur.text=self.ids.i2.text
	def k3(self):
		global top
		top=self.ids.i3.text
		self.ids.kur.text=self.ids.i3.text
	def k4(self):
		global top
		top=self.ids.i4.text
		self.ids.kur.text=self.ids.i4.text
	def k5(self):
		global top
		top=self.ids.i5.text
		self.ids.kur.text=self.ids.i5.text
	def k6(self):
		global top
		top=self.ids.i6.text
		self.ids.kur.text=self.ids.i6.text
	def k7(self):
		global top
		top=self.ids.i7.text
		self.ids.kur.text=self.ids.i7.text
	def k8(self):
		global top
		top=self.ids.i8.text
		self.ids.kur.text=self.ids.i8.text
	def k9(self):
		global top
		top=self.ids.i9.text
		self.ids.kur.text=self.ids.i9.text
	def k10(self):
		global top
		top=self.ids.i10.text
		self.ids.kur.text=self.ids.i10.text
	def k11(self):
		global top
		top=self.ids.i11.text
		self.ids.kur.text=self.ids.i11.text
	def k12(self):
		global top
		top=self.ids.i12.text
		self.ids.kur.text=self.ids.i12.text


	def v1(self):
		global x
		x = str(self.ids.b1.text)
		self.ids.b1.text+=str(top)
		return self.joyla()
	def v2(self):
		global x
		x = str(self.ids.b2.text)
		self.ids.b2.text+=str(top)
		return self.joyla()
	def v3(self):
		global x
		x = str(self.ids.b3.text)
		self.ids.b3.text+=str(top)
		return self.joyla()
	def v4(self):
		global x
		x = str(self.ids.b4.text)
		self.ids.b4.text+=str(top)
		return self.joyla()
	def v5(self):
		global x
		x = str(self.ids.b5.text)
		self.ids.b5.text+=str(top)
		return self.joyla()
	def v6(self):
		global x
		x = str(self.ids.b6.text)
		self.ids.b6.text+=str(top)
		return self.joyla()
	def v7(self):
		global x
		x = str(self.ids.b7.text)
		self.ids.b7.text+=str(top)
		return self.joyla()
	def v8(self):
		global x
		x = str(self.ids.b8.text)
		self.ids.b8.text+=str(top)
		return self.joyla()
	def v9(self):
		global x
		x = str(self.ids.b9.text)
		self.ids.b9.text+=str(top)
		return self.joyla()
	def v10(self):
		global x
		x = str(self.ids.b10.text)
		self.ids.b10.text+=str(top)
		return self.joyla()
	def v11(self):
		global x
		x = str(self.ids.b11.text)
		self.ids.b11.text+=str(top)
		return self.joyla()
	def v12(self):
		global x
		x = str(self.ids.b12.text)
		self.ids.b12.text+=str(top)
		return self.joyla()
	def v13(self):
		global x
		x = str(self.ids.b13.text)
		self.ids.b13.text+=str(top)
		return self.joyla()
	def v14(self):
		global x
		x = str(self.ids.b14.text)
		self.ids.b14.text+=str(top)
		return self.joyla()
	def v15(self):
		global x
		x = str(self.ids.b15.text)
		self.ids.b15.text+=str(top)
		return self.joyla()
	def v16(self):
		global x
		x = str(self.ids.b16.text)
		self.ids.b16.text+=str(top)
		return self.joyla()
	def v17(self):
		global x
		x = str(self.ids.b17.text)
		self.ids.b17.text+=str(top)
		return self.joyla()
	def v18(self):
		global x
		x = str(self.ids.b18.text)
		self.ids.b18.text+=str(top)
		return self.joyla()
	def v19(self):
		global x
		x = str(self.ids.b19.text)
		self.ids.b19.text+=str(top)
		return self.joyla()
	def v20(self):
		global x
		x = str(self.ids.b20.text)
		self.ids.b20.text+=str(top)
		return self.joyla()
	def v21(self):
		global x
		x = str(self.ids.b21.text)
		self.ids.b21.text+=str(top)
		return self.joyla()
	def v22(self):
		global x
		x = str(self.ids.b22.text)
		self.ids.b22.text+=str(top)
		return self.joyla()
	def v23(self):
		global x
		x = str(self.ids.b23.text)
		self.ids.b23.text+=str(top)
		return self.joyla()
	def v24(self):
		global x
		x = str(self.ids.b24.text)
		self.ids.b24.text+=str(top)
		return self.joyla()
	def v25(self):
		global x
		x = str(self.ids.b25.text)
		self.ids.b25.text+=str(top)
		return self.joyla()
	def v26(self):
		global x
		x = str(self.ids.b26.text)
		self.ids.b26.text+=str(top)
		return self.joyla()
	def v27(self):
		global x
		x = str(self.ids.b27.text)
		self.ids.b27.text+=str(top)
		return self.joyla()
	def v28(self):
		global x
		x = str(self.ids.b28.text)
		self.ids.b28.text+=str(top)
		return self.joyla()
	def v29(self):
		global x
		x = str(self.ids.b29.text)
		self.ids.b29.text+=str(top)
		return self.joyla()
	def v30(self):
		global x
		x = str(self.ids.b30.text)
		self.ids.b30.text+=str(top)
		return self.joyla()
	def v31(self):
		global x
		x = str(self.ids.b31.text)
		self.ids.b31.text+=str(top)
		return self.joyla()
	def v32(self):
		global x
		x = str(self.ids.b32.text)
		self.ids.b32.text+=str(top)
		return self.joyla()
	def v33(self):
		global x
		x = str(self.ids.b33.text)
		self.ids.b33.text+=str(top)
		return self.joyla()
	def v34(self):
		global x
		x = str(self.ids.b34.text)
		self.ids.b34.text+=str(top)
		return self.joyla()
	def v35(self):
		global x
		x = str(self.ids.b35.text)
		self.ids.b35.text+=str(top)
		return self.joyla()
	def v36(self):
		global x
		x = str(self.ids.b36.text)
		self.ids.b36.text+=str(top)
		return self.joyla()
	def v37(self):
		global x
		x = str(self.ids.b37.text)
		self.ids.b37.text+=str(top)
		return self.joyla()
	def v38(self):
		global x
		x = str(self.ids.b38.text)
		self.ids.b38.text+=str(top)
		return self.joyla()
	def v39(self):
		global x
		x = str(self.ids.b39.text)
		self.ids.b39.text+=str(top)
		return self.joyla()
	def v40(self):
		global x
		x = str(self.ids.b40.text)
		self.ids.b40.text+=str(top)
		return self.joyla()
	def v41(self):
		global x
		x = str(self.ids.b41.text)
		self.ids.b41.text+=str(top)
		return self.joyla()
	def v42(self):
		global x
		x = str(self.ids.b42.text)
		self.ids.b42.text+=str(top)
		return self.joyla()
	def v43(self):
		global x
		x = str(self.ids.b43.text)
		self.ids.b43.text+=str(top)
		return self.joyla()
	def v44(self):
		global x
		x = str(self.ids.b44.text)
		self.ids.b44.text+=str(top)
		return self.joyla()
	def v45(self):
		global x
		x = str(self.ids.b45.text)
		self.ids.b45.text+=str(top)
		return self.joyla()
	def v46(self):
		global x
		x = str(self.ids.b46.text)
		self.ids.b46.text+=str(top)
		return self.joyla()
	def v47(self):
		global x
		x = str(self.ids.b47.text)
		self.ids.b47.text+=str(top)
		return self.joyla()
	def v48(self):
		global x
		x = str(self.ids.b48.text)
		self.ids.b48.text+=str(top)
		return self.joyla()
	def v49(self):
		global x
		x = str(self.ids.b49.text)
		self.ids.b49.text+=str(top)
		return self.joyla()
	def v50(self):
		global x
		x = str(self.ids.b50.text)
		self.ids.b50.text+=str(top)
		return self.joyla()
	def v51(self):
		global x
		x = str(self.ids.b51.text)
		self.ids.b51.text+=str(top)
		return self.joyla()
	def v52(self):
		global x
		x = str(self.ids.b52.text)
		self.ids.b52.text+=str(top)
		return self.joyla()
	def v53(self):
		global x
		x = str(self.ids.b53.text)
		self.ids.b53.text+=str(top)
		return self.joyla()
	def v54(self):
		global x
		x = str(self.ids.b54.text)
		self.ids.b54.text+=str(top)
		return self.joyla()
	def v55(self):
		global x
		x = str(self.ids.b55.text)
		self.ids.b55.text+=str(top)
		return self.joyla()
	def v56(self):
		global x
		x = str(self.ids.b56.text)
		self.ids.b56.text+=str(top)
		return self.joyla()
	def v57(self):
		global x
		x = str(self.ids.b57.text)
		self.ids.b57.text+=str(top)
		return self.joyla()
	def v58(self):
		global x
		x = str(self.ids.b58.text)
		self.ids.b58.text+=str(top)
		return self.joyla()
	def v59(self):
		global x
		x = str(self.ids.b59.text)
		self.ids.b59.text+=str(top)
		return self.joyla()
	def v60(self):
		global x
		x = str(self.ids.b60.text)
		self.ids.b60.text+=str(top)
		return self.joyla()
	def v61(self):
		global x
		x = str(self.ids.b61.text)
		self.ids.b61.text+=str(top)
		return self.joyla()
	def v62(self):
		global x
		x = str(self.ids.b62.text)
		self.ids.b62.text+=str(top)
		return self.joyla()
	def v63(self):
		global x
		x = str(self.ids.b63.text)
		self.ids.b63.text+=str(top)
		return self.joyla()
	def v64(self):
		global x
		x = str(self.ids.b64.text)
		self.ids.b64.text+=str(top)
		return self.joyla()
	def v65(self):
		global x
		x = str(self.ids.b65.text)
		self.ids.b65.text+=str(top)
		return self.joyla()
	def v66(self):
		global x
		x = str(self.ids.b66.text)
		self.ids.b66.text+=str(top)
		return self.joyla()
	def v67(self):
		global x
		x = str(self.ids.b67.text)
		self.ids.b67.text+=str(top)
		return self.joyla()
	def v68(self):
		global x
		x = str(self.ids.b68.text)
		self.ids.b68.text+=str(top)
		return self.joyla()
	def v69(self):
		global x
		x = str(self.ids.b69.text)
		self.ids.b69.text+=str(top)
		return self.joyla()
	def v70(self):
		global x
		x = str(self.ids.b70.text)
		self.ids.b70.text+=str(top)
		return self.joyla()
	def v71(self):
		global x
		x = str(self.ids.b71.text)
		self.ids.b71.text+=str(top)
		return self.joyla()
	def v72(self):
		global x
		x = str(self.ids.b72.text)
		self.ids.b72.text+=str(top)
		return self.joyla()
	def v73(self):
		global x
		x = str(self.ids.b73.text)
		self.ids.b73.text+=str(top)
		return self.joyla()
	def v74(self):
		global x
		x = str(self.ids.b74.text)
		self.ids.b74.text+=str(top)
		return self.joyla()
	def v75(self):
		global x
		x = str(self.ids.b75.text)
		self.ids.b75.text+=str(top)
		return self.joyla()
	def v76(self):
		global x
		x = str(self.ids.b76.text)
		self.ids.b76.text+=str(top)
		return self.joyla()
	def v77(self):
		global x
		x = str(self.ids.b77.text)
		self.ids.b77.text+=str(top)
		return self.joyla()
	def v78(self):
		global x
		x = str(self.ids.b78.text)
		self.ids.b78.text+=str(top)
		return self.joyla()
	def v79(self):
		global x
		x = str(self.ids.b79.text)
		self.ids.b79.text+=str(top)
		return self.joyla()
	def v80(self):
		global x
		x = str(self.ids.b80.text)
		self.ids.b80.text+=str(top)
		return self.joyla()
	def v81(self):
		global x
		x = str(self.ids.b81.text)
		self.ids.b81.text+=str(top)
		return self.joyla()
	def v82(self):
		global x
		x = str(self.ids.b82.text)
		self.ids.b82.text+=str(top)
		return self.joyla()
	def v83(self):
		global x
		x = str(self.ids.b83.text)
		self.ids.b83.text+=str(top)
		return self.joyla()
	def v84(self):
		global x
		x = str(self.ids.b84.text)
		self.ids.b84.text+=str(top)
		return self.joyla()
	def v85(self):
		global x
		x = str(self.ids.b85.text)
		self.ids.b85.text+=str(top)
		return self.joyla()
	def v86(self):
		global x
		x = str(self.ids.b86.text)
		self.ids.b86.text+=str(top)
		return self.joyla()
	def v87(self):
		global x
		x = str(self.ids.b87.text)
		self.ids.b87.text+=str(top)
		return self.joyla()
	def v88(self):
		global x
		x = str(self.ids.b88.text)
		self.ids.b88.text+=str(top)
		return self.joyla()
	def v89(self):
		global x
		x = str(self.ids.b89.text)
		self.ids.b89.text+=str(top)
		return self.joyla()
	def v90(self):
		global x
		x = str(self.ids.b90.text)
		self.ids.b90.text+=str(top)
		return self.joyla()



	def joyla(self):
		global w3
		global w4
		global w5
		global w7
		global w9
		global w11
		global w13
		global e1
		global e2
		global e3
		global e4
		global e5
		global e6
		global j

		if str(top)=='y4':
			w4+=1
			j+=1
			self.ids.yul4.text+=str(x+',')
			self.ids.yu4.text=str(w4)
			self.ids.summ.text=str(j)
		if str(top)=='y3':
			w3+=1
			j+=1
			self.ids.yul3.text+=str(x+',')
			self.ids.yu3.text=str(w3)
			self.ids.summ.text=str(j)
		if str(top)=='y5':
			w5+=1
			j+=1
			self.ids.yul5.text+=str(x+',')
			self.ids.yu5.text=str(w5)
			self.ids.summ.text=str(j)
		if str(top)=='y7':
			w7+=1
			j+=1
			self.ids.yul7.text+=str(x+',')
			self.ids.yu7.text=str(w7)
			self.ids.summ.text=str(j)
		if str(top)=='y9':
			w9+=1
			j+=1
			self.ids.yul9.text+=str(x+',')
			self.ids.yu9.text=str(w9)
			self.ids.summ.text=str(j)
		if str(top)=='y11':
			w11+=1
			j+=1
			self.ids.yul11.text+=str(x+',')
			self.ids.yu11.text=str(w11)
			self.ids.summ.text=str(j)
		if str(top)=='y13':
			w13+=1
			j+=1
			self.ids.yul13.text+=str(x+',')
			self.ids.yu13.text=str(w13)
			self.ids.summ.text=str(j)
		if str(top)=='s1':
			e1+=1
			j+=1
			self.ids.sef1.text+=str(x+',')
			self.ids.se1.text=str(e1)
			self.ids.summ.text=str(j)
		if str(top)=='s2':
			e2+=1
			j+=1
			self.ids.sef2.text+=str(x+',')
			self.ids.se2.text=str(e2)
			self.ids.summ.text=str(j)
		if str(top)=='s3':
			e3+=1
			j+=1
			self.ids.sef3.text+=str(x+',')
			self.ids.se3.text=str(e3)
			self.ids.summ.text=str(j)
		if str(top)=='s4':
			e4+=1
			j+=1
			self.ids.sef4.text+=str(x+',')
			self.ids.se4.text=str(e4)
			self.ids.summ.text=str(j)
		if str(top)=='s5':
			e5+=1
			j+=1
			self.ids.sef5.text+=str(x+',')
			self.ids.se5.text=str(e5)
			self.ids.summ.text=str(j)
		if str(top)=='s6':
			e6+=1
			j+=1
			self.ids.sef6.text+=str(x+',')
			self.ids.se6.text=str(e6)
			self.ids.summ.text=str(j)



class Page_LayoutApp(App):
	def build(self):
		return PageLayout()

if __name__ == '__main__':
	Page_LayoutApp().run()
