use yew::prelude::*;
use serde::Deserialize;
use gloo_net::http::Request;
use wasm_bindgen_futures::spawn_local;
use web_sys::console;


use wasm_bindgen::prelude::*;

// Define the data structure expected from the backend API
#[derive(Deserialize, Debug, Clone)]
struct Group {
    id: i32,
    name: String,
    number: i32,
}

// Define the main App component
#[function_component(App)]
fn app() -> Html {
    // State to hold the list of groups
    let groups = use_state(|| Vec::new());
    // State to hold any errors
    let error = use_state(|| None::<String>);

    {
        // Clone the states to move into the closure
        let groups = groups.clone();
        let error = error.clone();
        // Effect hook to fetch data when the component mounts
        use_effect_with_deps(move |_| {
            // Spawn a local future to perform the async request
            spawn_local(async move {
                match Request::get("http://localhost:8000/groups/")
                    .send()
                    .await
                {
                    Ok(response) => {
                        if response.ok() {
                            match response.json::<Vec<Group>>().await {
                                Ok(data) => groups.set(data),
                                Err(err) => error.set(Some(format!("Error parsing JSON: {}", err))),
                            }
                        } else {
                            error.set(Some(format!("HTTP Error: {}", response.status())));
                        }
                    },
                    Err(err) => error.set(Some(format!("Request error: {}", err))),
                }
            });
            // Cleanup function
            || ()
        }, ());
    }

    // Render the HTML based on the state
    html! {
        <div>
            <h1>{ "Atomic Simulation" }</h1>
            {
                if let Some(err) = &*error {
                    html! { <p style="color: red;">{ err }</p> }
                } else if groups.is_empty() {
                    html! { <p>{ "Loading..." }</p> }
                } else {
                    html! {
                        <ul>
                            { for groups.iter().map(|group| html! {
                                <li>{ format!("{} - {}", group.name, group.number) }</li>
                            }) }
                        </ul>
                    }
                }
            }
        </div>
    }
}

// Entry point for the WASM module
#[wasm_bindgen(start)]
pub fn run_app() {
    yew::Renderer::<App>::new().render();
}
