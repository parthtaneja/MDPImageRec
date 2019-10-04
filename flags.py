flags=["Cambodia.jpg","Laos.jpg","Malaysia.jpg","Myanmar.jpg","Philippines.jpg","Singapore.jpg","Thailand.jpg","Vietnam.jpg","Indonesia.jpg","Brunei.jpg"]   

    while True:
           methods = 'cv2.TM_CCOEFF_NORMED'
           list_of_pics=[]
           for flag in flags:
                   template= cv2.imread(flag,0)
                   img = cv2.imread('philippines2.jpg',0)

    # generate Gaussian pyramid for A
                    G = template.copy()
                    gpA = [G]
                    for i in xrange(6):
                            G = cv2.pyrDown(G)
                            gpA.append(G)


                    n=0
                    for x in gpA:       

                           w, h = x.shape[::-1]


                           method = eval(methods)#

            # Apply template Match
                          res = cv2.matchTemplate(img,x,method)
                          matchVal=res[0][0]
                          picDict={"matchVal":matchVal,"name":flag}
                          list_of_pics.append(picDict)

                           n=n+1
        newlist = sorted(list_of_pics, key=operator.itemgetter('matchVal'),reverse=True) 
#print newlist
        matched_image=newlist[0]['name']
print matched_image
k=cv2.waitKey(10)
if (k==27):
    break
cv2.destroyAllWindows()
