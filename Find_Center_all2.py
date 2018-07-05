from PIL import Image, ImageDraw, ImageFilter, ImageTk, ImageOps
import tkinter.filedialog
import math
import os
from pathlib import Path

##tk=tkinter.Tk()
##image=tkinter.filedialog.askopenfilename()
##tk.destroy()
# 위의 세 줄을 통하여 이미지 이름을 읽어옴.

#base directory
drbase = "G:\Photo_works/20090722.PSE.350/raw/"
#read directory(input data)
drin = "TIFF16/"
#write directory(output data)
drout = 'crop/'


for image in sorted(os.listdir(drbase+drin)):
    #check tif files
	#my_file = Path("%s\%s\%s_crop.tif") %(drbase, drout, image[-23:-4])
	my_file = Path(drbase+drout+image[-23:-4]+"_crop.tif")
	if my_file.is_file():
		print (drbase+drout+image[-23:-4]+"_crop.tif is already exist")
		#print ("%s\%s\%s_crop.tif is already exist") %(drbase, drout, image[-23:-4])
		
	elif image[-4:] == '.TIF':
    
		image = drbase+drin+image
		dx=[0,1,0,-1]  # BFS x변화값
		dy=[1,0,-1,0]  # BFS y변화값
		
		
		im1=Image.open(image) # 이미지 읽어옴
		width=im1.width       # 가로
		height=im1.height     # 세로
		
		#시간복잡도 줄이기 위해 배열 크기 최소화를 위해 mn,mx 선언
		mx=0
		mn=0
		if(width>height):
			mx=width
			mn=height
		else:
			mx=height
			mn=width
		im=Image.new("RGB",(mn,mn)) #새로 작성할 이미지
		
		s=0
		x=[[0 for col in range(height+1)] for row in range(width+1)]
		v=[[0 for col in range(height+1)] for row in range(width+1)]
		
		a=[0]*mn*2
		b=[0]*mn*2
		P=[0]*width*height
		Q=[0]*width*height
		
		#픽셀 받아옴
		arr=im1.getdata()
		sz=0
		
		
		#검정인가 아닌가
		for i in range(0,width):
			for j in range(0,height):
				o=arr[j*width+i]
				s=o[0]+o[1]+o[2]
				if(s<40):
					x[i][j]=1;
				else:
					x[i][j]=0;
		
		
		front=0
		end=1
		v[0][0]=1
		P[0]=0
		Q[0]=0
		
		
		#BFS
		while(end-front!=0):
			p=P[front]
			q=Q[front]
			front+=1
			for k in range(0,4):
				r=p+dx[k]
				s=q+dy[k]
				if(r>=0 and s>=0 and r<width and s<height):
		
					if(v[r][s]==0):
						if(x[r][s]==1):
							v[r][s]=1
							P[end]=r
							Q[end]=s
							end+=1
						else:
							v[r][s]=1
							a[sz]=r
							b[sz]=s
							sz+=1
		
		
		# 최소, 최대, 차 함수 정의
		def min(A,B):
			if(A>B):
				return B
			else:
				return A
			
		def max(A,B):
			if(A<B):
				return B
			else:
				return A
		def abs(A,B):
			if(A<B):
				return B-A
			else:
				return A-B
		p=1
		q=mn*mn
		d=[[0 for col in range(height+1)] for row in range(width+1)]
		
		
		#이진탐색과 변화값 배열
		while(q-p!=1):
			h=(p+q)//2
			for i in range(0,width):
				for j in range(0,height):
					d[i][j]=0
			for i in range(0,sz):
				r=a[i]
				s=b[i]
				H=int(math.sqrt(h))
				st=max(0,r-H)
				en=min(width-1,r+H)
				for j in range(st,en+1):
					sq=h-abs(r,j)*abs(r,j)
					sqr=int(math.sqrt(sq))
					d[j][max(s-sqr,0)]+=1
					d[j][min(s+sqr,height-1)+1]-=1
			check=0
			for i in range(0,width):
				c=0
				if(check==1):
					break
				for j in range(0,height):
					c+=d[i][j]
					d[i][j]=c
					if(d[i][j]>=sz):
						check=1
						break
			if(check==1):
				q=h
			else:
				p=h
		
		
		mm=0
		h=q
		ans1=-1
		ans2=0
		
		#이진탐색으로 구한 반지름에서의 중심 찾기
		for i in range(0,width):
			for j in range(0,height):
				d[i][j]=0
		for i in range(0,sz):
			r=a[i]
			s=b[i]
			H=int(math.sqrt(h))
			st=max(0,r-H)
			en=min(width-1,r+H)
			for j in range(st,en+1):
				sq=h-abs(r,j)*abs(r,j)
				sqr=int(math.sqrt(sq))
				d[j][max(s-sqr,0)]+=1
				d[j][min(s+sqr,height-1)+1]-=1
		for i in range(0,width):
			c=0
			if(ans1!=-1):
				break
			for j in range(0,height):
				c+=d[i][j]
				d[i][j]=c
				if(d[i][j]>=sz):
					ans1=i
					ans2=j
					break           
		
		
		#이미지 최종 편집
		centx=int(mn//2)
		centy=int(mn//2)
		for i in range(0,mn):
			for j in range(0,mn):
				cx=i-centx
				cy=j-centy
				if(ans1+cx<0 or ans1+cx>=width or ans2+cy<0 or ans2+cy>=height):
					im.putpixel((i,j),(0,0,0))
				else:
					im.putpixel((i,j),arr[(ans2+cy)*width+ans1+cx])
		
		
		#저장
		#im.save("%s\%s\%s_crop.tif") %(drbase, drout, image[-23:-4])
		im.save(drbase+drout+image[-23:-4]+"_crop.tif")
		print (drbase+drout+image[-23:-4]+"_crop.tif is created")
		#print ("%s\%s\%s_crop.tif is created") %(drbase, drout, image[-23:-4])
				
