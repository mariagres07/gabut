class maria{
    String nama;
    int umur;
    String impian;
    String favgroup;
    String wishlist;

    maria(String nama, int umur, String impian, String favgroup, String wishlist){
        this.nama = nama;
        this.umur = umur;
        this.impian = impian;
        this.favgroup = favgroup;
        this.wishlist = wishlist;
    }

    void display(){
        System.out.println("Nama Lengkap : " + this.nama);
        System.out.println("Umur         : " + this.umur);
        System.out.println("Impian       : " + this.impian);
        System.out.println("Kpop group   : " + this.favgroup);
        System.out.println("Wishlist     : " + this.wishlist);
    }
}

public class latihanmaria {
    public static void main(String[] args) {
        maria data = new maria("maria", 18, "orkay", "nctdream", "skincare");
        maria data1 = new maria("flo", 19, "sama lano", "nct", "pacaran sama lano");
        maria data2 = new maria("lia", 19, "pacaran sama ian", "treasure", "sama ian pokoknya");
        data.display();
        System.out.println();
        data1.display();
        System.out.println();
        data2.display();
    }
}