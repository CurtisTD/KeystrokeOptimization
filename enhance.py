from sklearn import preprocessing 
from sklearn.decomposition import PCA

def enhancement(template, query, k):
    #these are scalers focused on scaling the data
    if k == 1:
        ss = preprocessing.StandardScaler()
        #outliers can shrink the range of feature values
        #is very sensitive to the prescence of outliers
        ss.fit(template)
        template = ss.transform(template) #stardardizes by centering and scaling
        query = ss.transform(query)
        
    elif k == 2:
        rs = preprocessing.RobustScaler()
        #not affected by few large outliers, where other scalers would be
        rs.fit(template)
        template = rs.transform(template) #centers and scales the data
        query = rs.transform(query) 
        
    elif k == 3:
        mm = preprocessing.MinMaxScaler()
        #rescales the data set such that all feature values are in the range [0, 1]
        #compresses inliers to a range
        #also very sensitive to the prescence of outliers
        mm.fit(template)
        template = mm.transform(template)
        query = mm.transform(query)           
        
    elif k == 4:
        pca = PCA(n_components=5)
        #
        pca.fit(template)
        template = pca.transform(template)
        query = pca.transform(query)
        
    else:
        print("No enhancement applied. Returning original data.")
        
    return template, query
