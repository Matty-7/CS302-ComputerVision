camera {
  location <4, 0.5, 0.5>  
  look_at <0.5, 0.5, 0.5>
}

light_source { <4, 2, 0> color rgb <1, 1, 1> }

plane { <0, 1, 0>, 0
    texture { pigment { color rgb <1, 1, 1> } }
}

box { <0, 0, 0>, <1, 1, 1>
    texture {Chrome_Metal}  
}

box { <1.5, 0, 0>, <2.5, 1, 1>
    texture {Brass_Metal}
}
