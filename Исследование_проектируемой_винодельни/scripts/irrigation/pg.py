import sys,pypdf
r=pypdf.PdfReader(sys.argv[1]); 
for n in sys.argv[3:]:
    w=pypdf.PdfWriter(); w.add_page(r.pages[int(n)-1]); w.write(f"{sys.argv[2]}_p{n}.pdf")
