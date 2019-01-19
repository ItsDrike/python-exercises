import Solution3


def test_main_alphabet_order():
    result = Solution.main('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    assert result == 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'

    result = Solution.main('Z Y X W V U T S R Q P O N M L K J I H G F E D C B A')
    assert result == 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'

    result = Solution.main('aAaa aBaa aAab aAba a bAaa bAba bAab bAbb bBbb bBba bBab bBaa b c d e f g j kKklmn o pq str')
    assert result == 'a,aAaa,aAab,aAba,aBaa,b,bAaa,bAab,bAba,bAbb,bBaa,bBab,bBba,bBbb,c,d,e,f,g,j,kKklmn,o,pq,str'


def test_main_duplicate_elimination():
    result = Solution.main('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    assert result == 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'

    result = Solution.main('A A A A A A B B A B B A B B A B A B B B A C B A B B B A A D A B B A B F B A B F F F F L F F F P F N')
    assert result == 'A,B,C,D,F,L,N,P'


def test_main_multiple_spaces():
    result = Solution.main('     k     o     h n  kkk h u gh uof  fu       i    g   o  v')
    assert result == 'fu,g,gh,h,i,k,kkk,n,o,u,uof,v'
