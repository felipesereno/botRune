use enigo::{Enigo, MouseControllable, MouseButton};


fn mouse_click(x: u16, y: u16){
    let mut enigo: Enigo = Enigo::new();

    // Movendo o mouse para uma posição específica (x, y)
    enigo.mouse_move_to(x as i32, y as i32);

    // Pressionando e soltando o botão esquerdo do mouse
    enigo.mouse_down(MouseButton::Left);
    enigo.mouse_up(MouseButton::Left);
}


fn main() {
    
}
