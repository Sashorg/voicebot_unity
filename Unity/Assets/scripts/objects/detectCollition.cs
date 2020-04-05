using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Windows.Speech;
using System.IO;

public class detectCollition : MonoBehaviour
{
[SerializeField]
private Text m_Hypotheses;
public string name;
public static string speech="";
    public delegate void SendMsg();

    
    public static event SendMsg sendMsg;
    [SerializeField]
    private Text m_Recognitions;

 private DictationRecognizer m_DictationRecognizer;
  public  static bool start_translate=false;
    public static bool stop_translate = false;
    
    // Start is called before the first frame update
    void Start()
    {
       
    }

    // Update is called once per frame
    void Update()
    {
       
    }
    void CreateText(string json) {
        string path = "C:\\Users\\1254-\\PycharmProjects\\chatbot2\\who_is_bot.json";
        
            File.WriteAllText(path, json);
        
    }
    private void OnTriggerEnter(Collider other)
    {
        string json = "{\"name\":\"" + name + "\" }";
        CreateText(json);
        m_DictationRecognizer = new DictationRecognizer();

        m_DictationRecognizer.DictationResult += (text, confidence) =>
        {
            speech = text;
            NetworkManager networkManager = new NetworkManager();
            if (sendMsg != null)
                sendMsg();
            NetworkManager.once = 0;
            m_DictationRecognizer.Stop();
            Invoke("newVoid", 4);
            Debug.LogFormat("Dictation result: {0}", text);
            m_Recognitions.text += text + "\n";
            Debug.LogFormat("Dictation speech: {0}", speech);

        };

        m_DictationRecognizer.DictationHypothesis += (text) =>
        {
            Debug.LogFormat("Dictation hypothesis: {0}", text);
          //  m_Hypotheses.text += text;
        };

        m_DictationRecognizer.DictationComplete += (completionCause) =>
        {
            if (completionCause != DictationCompletionCause.Complete)
                Debug.LogErrorFormat("Dictation completed unsuccessfully: {0}.", completionCause);
        };

        m_DictationRecognizer.DictationError += (error, hresult) =>
        {
            Debug.LogErrorFormat("Dictation error: {0}; HResult = {1}.", error, hresult);
        };

        m_DictationRecognizer.Start();
        print("result");
        print(m_DictationRecognizer);
    }

    private void OnTriggerExit(Collider other)
    {
        m_DictationRecognizer.Stop();
        Debug.Log("Ciao");
    }
    void newVoid()
    {
        m_DictationRecognizer.Start();
        //things you wanna do after 2 seconds...
    }

}
