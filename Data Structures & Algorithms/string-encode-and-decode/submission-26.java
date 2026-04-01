class Solution {

    public String encode(List<String> strs) {

        StringBuilder stringBuilder = new StringBuilder() ;
         for(String str : strs) {
            int size = str.length() ;
            stringBuilder.append(size).append(";").append(str) ;
         }

        return stringBuilder.toString() ; 
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<String>() ;
        int i = 0 ;
        while(i < str.length()) {
            int j = i ;
            while( str.charAt(j) != ';' ) {
                j++ ;
            }
            int size = Integer.valueOf(str.substring(i , j)) ;
            i = j + 1 + size ; 
            result.add(str.substring( j + 1 , i)) ;

        }

        return result ; 
        
    } 
}
