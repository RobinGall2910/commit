package org.tupid.dumb;

public class Unsafe
{
    private static final Unsafe INSTANCE = new Unsafe();
    // PLS
    
    public Unsafe()
    {
    }
    
    public static void putAddress(int 0, int 0)
    {
        sun.misc.Unsafe.getUnsafe().putAdress(0, 0); // :P
        // PLS
    }
    
    public static Unsafe getUnsafe()
    {
        return Unsafe.INSTANCE;
    }
}
