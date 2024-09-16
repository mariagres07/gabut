class buku {

    String judul;
    String penulis;

    buku(String judul, String penulis) {
        this.judul = judul;
        this.penulis = penulis;
    }

    void tampilan() {
        System.out.println("\nJudul\t : " + this.judul);
        System.out.println("Penulis\t : " + this.penulis);
    }
}

public class lat8 {

    public static void main(String[] args) {
        buku buku1 = new buku("Harry Potter", "J.K Rowling");
        buku1.tampilan();

        String addressbuku1 = Integer.toHexString(System.identityHashCode(buku1));
        System.out.println(addressbuku1);

        buku buku2 = new buku("Harry Potter", "J.K Rowling");
        buku2.tampilan();
        String addressbuku2 = Integer.toHexString(System.identityHashCode(buku2));
        System.out.println(addressbuku2);

        buku1.judul = "maria cantik";
        buku1.tampilan();
        buku2.tampilan();
    }
}
