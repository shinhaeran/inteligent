import java.sql.*;
public class test {
    public static void main(String[] args) {
        String u1 = "도손";
        tsetfunc1(u1);
        String u2 = "누리알찬";
        tsetfunc1(u2);
    }
    static void tsetfunc1(String user) {
        Connection con = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        try {
            Class.forName("org.mariadb.jdbc.Driver");
            con = DriverManager.getConnection(
                    "jdbc:mariadb://203.255.92.74/lhb_test1",
                    "root",
                    "1");
            pstmt = con.prepareStatement("select tmp.pn, tmp.ps, tmp.pj from \n" + //name, skinType, job
                    "(select prdt.productName as pn , prdt.skinType as ps , prdt.job as pj, count(1) as cnt\n" +
                    "FROM ux_product AS prdt, ux_user AS usr\n" + //prdt: ux_product, usr: ux_user
                    "WHERE usr.nickName = '"+user+"' and (prdt.gender = usr.gender or prdt.skinType = usr.skinType or prdt.job = usr.job)\n" +
                    "GROUP BY usr.nickName, prdt.productName ORDER BY cnt DESC limit 10) as tmp;");
            rs = pstmt.executeQuery();

            while(rs.next()) {
                String res = "";
                for(int i = 1; i < 4; i++) {
                    String tmp = rs.getString(i);
                    res = res.concat(tmp+", ");
                }
                System.out.println(user+" 님의 피부 타입에 맞는 화장품 추천 : "+res);
            }


        } catch(Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if(rs != null) {
                    rs.close();
                }

                if(pstmt != null) {
                    pstmt.close();
                }

                if(con != null) {
                    con.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}