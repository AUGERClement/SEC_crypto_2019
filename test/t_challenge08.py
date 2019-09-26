##
# Challenge08
##
# !/bin/python3

import unittest
from challenge08 import reader, AESDetect

class TestChallenge08(unittest.TestCase):
    my_input=["hbF6M/IBmZXZ11H5QHHNaI0QU+swH/GfXZcZuPWuxIG7wXhCl3mraeckbFb/cL2+",
                "NXQMSbuXH11s301Nj/4jWZqW9lgeGNnUVyVig2TFTblZYNlC0ElHnue+xJmzYVvT",
                "SaWpFf9qA9MC7JzSTS6a8VJiPebnoRhrexMBErFWjMkgO5IIYjznPSbzsU9M9hLN",
                "HY2UWi8+lCIzDEDo4BKIRubNqJR/Q7rxmAxo5ltE+pfW86clf+ZdswUyzDWU3Jho",
                "WAkKa2HAK0tO5rDdisKdO+m8h/VbSqDRl6PrB/Jb5HkJ/GihPTjhuhBnnUgl9iro",
                "i2gIW3AKJqDLhIedWXOsuhNSIEC5cAOa08lOb+0xCuCiJgQcf1xub0lX3d+XClj4",
                "6JbhJTtlKMA3Qge6hFB/25vgh+lbEn+vCHCJWGq81cu4RjZbtArM00fkoM4+nkq3",
                "cC6otLEabpae7nAlsZlv2azADIbXyxDnIWTQG6TgotNIyYtgOPGo9/53/tNPVqMY",
                "Y/nFx1HNuG0AWZgnRqe8UvVozBMQ6jbeYuMIGbH1XMFVLXxkSsVT9aoRCpV+EwIP",
                "B/XgY+esHNt+VfkI1XUMBVIQUv+JDKW4dNB61zm9IYIGmTZtM5BBHQB3dz8EZSkr",
                "j9xp7vDx4wZ7kR0msJuvmlQaRkTeTmItqMVHVm/gddRb6dhz774r4ijJm2mWghDX",
                "JiM350SPy91MYWQvHSPALQ1eBzbmE5D5o0mS60tEKeVfpoDBuDrilBV8Ruo/RJI8",
                "IceyNglirWM+FmYV6Hv6V5Ed1saqOc14k+5esjCy8cxGqFBlZEqBLfyP8lb7nm4y",
                "kH2G2PJq9Ux6a2KnS5zHRE0s+49dLqd4EibCr8aEGdYlXVxIdoIxEga52tD1pt9O",
                "h1VLmXXAbZ43CG0Bqn+kGodVS5l1wG2eNwhtAap/pBrE1kBC4kmaxN5VGr1d21wS",
                "Ld4cwV+udcEgdMS+5ezI0vUgSrWlspb8R+U9bp9Rbftz3cmNbHgIu0h76nrQsmLk",
                "t//1p9OCr+NxFCy/CxC4VGhki0eov8JI1vVPrLuu5lwOvlu7TVT8QrzjJowYs3yW",
                "xsNVATv/PU3axnGIBPqzMAkWl1XOaVVjfuyN+IxVrUoeRLNDytYiV6XX3yZ/g7O2",
                "PNJPtniImCT1cmChNlx700Bol7srtzAqnAw/AqDTtiDhYE4ouriQ5kNLZ8jrRj+4",
                "yXO/+Zc+ImjRGO5dnn2PflkTBaMijEKhTYL2zWsQ3Rn2GfHQZzbK9vZx4YecDEjn"]

    def test_read_file(self):
        self.assertEqual(reader("testFile/input08.txt"), self.my_input)

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)

    def test_pdf_example(self):
        self.assertEqual(AESDetect(self.my_input), 15)

    def test_pdf_example_reverse(self):
        self.assertEqual(AESDetect(self.my_input[::-1]), 6)

    def test_no_anwser(self):
        with self.assertRaises(SystemExit) as ret:
            AESDetect(self.my_input[0:10])
        self.assertEqual(ret.exception.code, 84)
