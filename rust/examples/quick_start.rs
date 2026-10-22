use crawlora_flashscore::{Client, FlashscoreSportsParams, ModelFlashscoreSportsResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.flashscore.sports(Default::default()).await?;
    let data: ModelFlashscoreSportsResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
