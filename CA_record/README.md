# Record the computer architecture I learned

## VIPT (Virtual Indexed Physical Tagged)
* Pre-understand: Physical cache(TLB more closly to CPU) v.s. Virtual cache
* VIPT try to get best of both
    * Can we access the cache at the same time as the TLB but still have the protection of VM?
    * Idea:
        * Look up in the cache with a `virtual address`
        * Verify that the data is right with a `physical tag`
    * Flow:
        * It'll gonna to use virtual index straight from CPU virtual addrss to look in cache and find the right cache line
        * Then get out the tag and the tag can get the physical address.
        * Will get the physical address from TLB and compare physical tag and physical address whether it will hit/miss.

```html
        ------> page offset  -> indexed the tag of the cache ->  Physical tag
        |
CPU  ---
        |
        ------> virtual page -> indexed the TLB              ->  Physical page

if (Physical tag == Physical page)
    hit!
```
#### Brain-storm
* With 4kB pages, how many bytes can a direct-mapped(1-way) VIPT cache store?
    * 4kB. We can only use the page offect bits(12 bits for 4kB pages) to index can only address 12 bits of address, or 4kB of data.
    * If we increase associativity, we can make it larger!
        * 8-way cache would give us 32kB of cache size(each way uses the same index.)

