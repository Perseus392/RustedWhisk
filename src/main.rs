use std::process::Command; //Dependencies to Execute Python using Command line arguments


fn main() {
    let mut wsk = Command::new("ibmcloud");
    let actioninvoke = wsk.arg("wsk").arg("action").arg("invoke").arg("--result").arg("hello").arg("--param-file").arg("parameters.json"); 
    match actioninvoke.output()
    {
        Ok(o) =>
        {
            unsafe{
                println!("Output: {}", String::from_utf8_unchecked(o.stdout));
            }
        },
 
        Err(e) => {
            println!("There was an error! {}",e);
        }
    }
}
