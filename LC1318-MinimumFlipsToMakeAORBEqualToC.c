int minFlips(int a, int b, int c){
    uint mask = 1;
    int flips = 0;
    int bit_a, bit_b, bit_c;

    for (int i=0; i<sizeof(int) * 8; i++) {
        mask = (uint) 1 << i;
        bit_a = a & mask;
        bit_b = b & mask;
        bit_c = c & mask;
        if ((bit_a | bit_b) != bit_c) {
            if ((bit_a > 0) && (bit_b > 0)) {
                flips += 2;
            } else {
                flips += 1;
            }
        }
    }

    return flips;
}


// Simple C code solution with bitwise operations. Note we need to use uint for mask variable.