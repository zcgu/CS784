import json
import codecs
import re

#get some statistics
def getList():
    
    type = u'Product Type'
    search = u'RAM Memory'
    
    productType_map = {}
    assembledLength_map = {}
    
    f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
    
    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split('?')
    
        json1 = json.loads(line_split[2])   # json for product 1
        json2 = json.loads(line_split[4])   # json for product 2
        
        if type in json1:
            type1 = json1[type][0]
            #print type1
            if type1 in productType_map:
                productType_map[type1] += 1
            else:
                productType_map[type1] = 1
            
            if search in json1:
                #print json1[search][0],'   ', type1              
                if type1 in assembledLength_map:
                    assembledLength_map[type1] += 1 
                else:
                    assembledLength_map[type1] = 1
            
        if type in json2:
            type2 = json2[type][0]
            #print type1
            if type2 in productType_map:
                productType_map[type2] += 1
            else:
                productType_map[type2] = 1
                
            if search in json2:
                if type2 in assembledLength_map:
                    assembledLength_map[type2] += 1 
                else:
                    assembledLength_map[type2] = 1
                    
                
    sorted_list = sorted(productType_map.items(), key=lambda d: d[1], reverse=True)
    
    sorted_list2 = sorted(assembledLength_map.items(), key=lambda d: d[1], reverse=True)
    
    #for tuple in sorted_list:
      #  print tuple
    
    return sorted_list
    

#find distribution
def outlier():
    
    type = u'Product Type'
    outlierType = u'Laptop Computers' #find outlier within same product type
    outlierSearch = u'RAM Memory'     #search criteria
    assembledLength_map = {}
    
    f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
    
    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split('?')
    
        json1 = json.loads(line_split[2])   # json for product 1
        json2 = json.loads(line_split[4])   # json for product 2
        
        if type in json1 and outlierSearch in json1:
            type1 = json1[type][0]
            if type1 == outlierType:
                value1 = json1[outlierSearch][0]
                value1 = int(re.sub("\D", "", value1))
                #print value1
                if value1 in assembledLength_map:
                    assembledLength_map[value1] += 1
                else:
                    assembledLength_map[value1] = 1
                 
            
        if type in json2 and outlierSearch in json2:
                    type2 = json2[type][0]
                    if type2 == outlierType:
                        value2 = json2[outlierSearch][0]
                        value2 = int(re.sub("\D", "", value2))
                        #print value2
                        if value2 in assembledLength_map:
                            assembledLength_map[value2] += 1
                        else:
                            assembledLength_map[value2] = 1
        else:
            continue
        
    sorted_list = sorted(assembledLength_map.items(), key=lambda d: d[0])
    
    for k in sorted(assembledLength_map.keys()):
        print k, '    ', assembledLength_map[k]
    return assembledLength_map  


    """ 
    for tuple in sorted_list:
        print tuple
    
    """
    

#list = getList() 

assembledLengthlist = outlier()

#for k in assembledLengthlist.keys():
  #  print k, '    ', assembledLengthlist[k]
    
    
    
    
