import json
import codecs
import re

#get some statistics
def getList():
    
    type = u'Product Type'
    search = u'Category'
    
    productType_map = {}
    category_map = {}
    
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
                if type1 in category_map:
                    category_map[type1] += 1 
                else:
                    category_map[type1] = 1
            
        if type in json2:
            type2 = json2[type][0]
            #print type1
            if type2 in productType_map:
                productType_map[type2] += 1
            else:
                productType_map[type2] = 1
                
            if search in json2:
                if type2 in category_map:
                    category_map[type2] += 1 
                else:
                    category_map[type2] = 1
                    
                
    sorted_list = sorted(productType_map.items(), key=lambda d: d[1], reverse=True)
    
    sorted_list2 = sorted(category_map.items(), key=lambda d: d[1], reverse=True)
    
    for tuple in sorted_list2:
        print tuple
    
    return sorted_list
    

#find distribution
def outlier():
    
    type = u'Product Type'
    outlierType = u'Laptop Computers' #find outlier within same product type
    outlierSearch = u'Product Long Description'     #search criteria
    descriptionLength_map = {}
    
    f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
    
    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split('?')
    
        json1 = json.loads(line_split[2])   # json for product 1
        json2 = json.loads(line_split[4])   # json for product 2
        
        if type in json1 and outlierSearch in json1:
            type1 = json1[type][0]
            #if type1 == outlierType:
            value1 = json1[outlierSearch][0]
            value1 = len(value1.split())
            if value1 == 1:
                print 'ID: ',line_split[1], ' Product Long Description: ', json1[outlierSearch][0]
            if value1 in descriptionLength_map:
                descriptionLength_map[value1] += 1
            else:
                descriptionLength_map[value1] = 1
                 
            
        if type in json2 and outlierSearch in json2:
                    type2 = json2[type][0]
                   # if type2 == outlierType:
                    value2 = json2[outlierSearch][0]
                    value2 = len(value2.split())
                    if value2 == 1:
                        print 'ID: ',line_split[3], ' Product Long Description: ',json2[outlierSearch][0]
                    if value2 in descriptionLength_map:
                        descriptionLength_map[value2] += 1
                    else:
                        descriptionLength_map[value2] = 1
        else:
            continue
        
    #sorted_list = sorted(descriptionLength_map.items(), key=lambda d: d[0], reverse=True)
    
    for k in sorted(descriptionLength_map.keys()):
        print k, '    ', descriptionLength_map[k]
    
    return descriptionLength_map  


    """ 
    for tuple in sorted_list:
        print tuple
    
    """
    

#list = getList() 

assembledLengthlist = outlier()

#for k in assembledLengthlist.keys():
  #  print k, '    ', assembledLengthlist[k]
    
    
    
    
