# include "colors.inc"

camera {
    location <0.5, 0.5, 6>
    look_at <0.5,0.5, 0>
}

light_source { <2, 4, 3> color rgb <1, 1, 1> }

plane {
    y, 0
    pigment { 
        checker 
        color Black
        color White
        scale 0.5
    } 
}

box { <0, 0, 0>, <1, 1, 1>
    texture {
        pigment { color rgb <1, 0, 0> }  // Red color
        finish { ambient 0.1 diffuse 0.9 }  // No reflectivity
} 
}

box { <1.5, 0, 0>, <2.5, 1, 1>
    texture {
        pigment { color rgb <0, 0, 1> }  // Blue color
        finish { ambient 0.1 diffuse 0.9 }  // No reflectivity
} 
}