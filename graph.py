class Graph:
    def __init__(self):
        g=[('root','a'),('a','b'),('a','d'),('b','j'),('b','c'),('b','g'),('j','k'),('k','l'),('k','m'),('c','i'),('c','o'),('d','e')
            ,('root','f'),('f','h'),('h','n'),('h','p'),('h','q'),('p','r'),('r','s')]
        a = {
            'label':'root'
            ,'children':[
                {
                    'label':'a'
                    ,'children':[
                        {
                            'label':'b'
                            ,'children':[
                                {
                                    'label':'c'
                                    ,'children':[
                                        {
                                            'label':'i'
                                            , 'children':[]
                                        }
                                    ]
                                }
                                ,{
                                    'label':'g'
                                    ,'children':[]
                                }
                            ]
                        }
                        ,{
                            'label':'d'
                            ,'children':[
                                {
                                    'label':'e'
                                    , 'children':[]
                                }
                            ]
                        }
                ]
                }
                , {
                    'label':'f'
                    , 'children':[
                        {
                            'label':'h'
                            , 'children':[]
                        }
                    ]
                }
            ]
            ,'back_func':'root_back_func'
            ,'enter_func':'root_enter_func'
            ,'parent':None
        }
        def init_do_func(ee,p=None,rst=[]):
            ee['back_func']=ee['label']+'_back_func'
            ee['enter_func']=ee['label']+'_enter_func'
            ee['parent']=p
        graph.walk(a,None,init_do_func)
        self.root=a
        self.root=graph.bords_to_graph(g)
    @staticmethod
    def bords_to_graph(bords):
        root={'label':'root','children':[],'back_func':'root_back_func','enter_func':'root_enter_func','parent':None}

        for b in bords:
            def append_child(ee):
                if b[0] == ee['label']:
                    c={'label':b[1],'children':[],'back_func':b[1]+'_back_func','enter_func':b[1]+'_enter_func','parent':ee}
                    ee['children'].append(c)
            graph.walk(root,append_child,rst=[])
        return root
    @staticmethod
    def is_adjacent(a,b):
        if a['label'] in [x['label'] for x in b['children']] or b['label'] in [x['label'] for x in a['children']]:
            return True
        else:
            return False
    @staticmethod
    def seed(src,dst):
        '''
        :param root:
        :param dst:
        :return:
        '''
        print('---------------seed start ... ------------------')
        st=[src]
        walked_st=[]
        path_st=[]
        while st:
            print([x['label'] for x in st], end='\t')
            e = st.pop()
            walked_st.append(e)
            walked_st_label=[x['label'] for x in walked_st]
            if path_st:
                #if (e['label'] in [x['label'] for x in path_st[-1]['children']]) or (path_st[-1]['parent'] and e['label'] ==path_st[-1]['parent']['label']):
                if graph.is_adjacent(e,path_st[-1]):
                    path_st.append(e)
                else:
                    while len(path_st)>1:
                        if not graph.is_adjacent(e,path_st[-1]):
                            path_st.pop()
                        else:
                            break
                    path_st.append(e)
            else:
                path_st.append(e)
            print(e['label'], end='\t')
            if e['parent'] and e['parent']['label'] not in walked_st_label :
                st.append(e['parent'])
            for ee in e['children'][::-1]:
                if ee['label'] not in walked_st_label :
                    st.append(ee)
            print([x['label'] for x in st])
            if e['label']==dst:
                break
        print('---------------seed end ------------------')
        print(walked_st_label)
        print([x['label'] for x in path_st])
        return e
    @staticmethod
    def walk(root,walk_func=None,walk_child_func=None,rst=[]):
        st = [root]
        while st:
            print([x['label'] for x in st],end='\t')
            e = st.pop()
            print(e['label'],end='\t')
            if walk_func:
                walk_func(e)
            for ee in e['children'][::-1]:
                if walk_child_func:
                    walk_child_func(ee, p=e, rst=rst)
                st.append(ee)
            print([x['label'] for x in st])
    def path(self,src,dst):
        src_obj = None
        src_label = None
        dst_obj = None
        dst_label=None
        if type(src) is str:
            src_label=src
        elif type(src) is dict:
            src_obj=src
            src_label=src_obj['label']
        if type(dst) is str:
            dst_label=dst
        elif type(dst) is dict:
            dst_obj=dst
            dst_label=dst_obj['label']
        path_st=[]
        st = [self.root]
        while st:
            e = st.pop()
            for ee in e['children']:
                st.append(ee)
                if not src_obj and ee['label'] == src:
                    pass
