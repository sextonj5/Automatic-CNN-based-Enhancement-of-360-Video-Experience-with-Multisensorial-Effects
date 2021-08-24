
package exhalia;


import java.util.NoSuchElementException;


public class CScentDiffusionContext {
  private int m_error;
  
  public final int DIFFUSER_ERROR_OK = 0;
  
  public final int DIFFUSER_ERROR_PARAMETER = 1;
  
  public final int DIFFUSER_ERROR_REGISTRY = 2;
  
  public final int DIFFUSER_ERROR_LIBRARY = 3;
  
  public String m_type;
  
  public String m_scent;
  
  public String m_disk;
  
  public String m_delay;
  
  public String m_duration;
  
  public String m_intensity;
  
  public String m_repeat;
  
  private native String __GetExhaliaVersion();
  
  private native void __LoadCartridge(boolean paramBoolean, String paramString);
  
  private native void __SetCartridge(boolean paramBoolean, String paramString1, String paramString2);
  
  private native void __Diffuse(String paramString1, String paramString2, String paramString3, String paramString4, String paramString5, String paramString6, String paramString7);
  
  public CScentDiffusionContext() {
    this.m_type = "";
    this.m_scent = "";
    this.m_disk = "";
    this.m_delay = "";
    this.m_duration = "";
    this.m_intensity = "";
    this.m_repeat = "";
    try {
      System.load("C:\\Users\\peldcu_1\\Desktop\\JohnsFiles\\exhaliaA\\src\\exhalia\\Exhalia.dll");
      this.m_error = 0;
    } catch (UnsatisfiedLinkError unsatisfiedLinkError) {
      System.err.println(unsatisfiedLinkError);
      this.m_error = 3;
    } 
  }
  
  public CScentDiffusionContext(String paramString1, String paramString2, String paramString3, String paramString4, String paramString5, String paramString6, String paramString7) {
    this();
    this.m_type = paramString1;
    this.m_scent = paramString2;
    this.m_disk = paramString3;
    this.m_delay = paramString4;
    this.m_duration = paramString5;
    this.m_intensity = paramString6;
    this.m_repeat = paramString7;
  }
  
  public String GetExhaliaVersion() {
    if (this.m_error != 3)
      return __GetExhaliaVersion(); 
    return "";
  }
  
  public int LoadCartridge(boolean paramBoolean, String paramString) {
    if (this.m_error != 3) {
      __LoadCartridge(paramBoolean, paramString);
      this.m_error = 0;
    } 
    return this.m_error;
  }
  
  public int SetCartridge(boolean paramBoolean, String paramString1, String paramString2) {
    if (this.m_error != 3) {
      __SetCartridge(paramBoolean, paramString1, paramString2);
      this.m_error = 0;
    } 
    return this.m_error;
  }
  
  public int Diffuse() {
    if (this.m_error != 3) {
      __Diffuse(this.m_type, this.m_scent, this.m_disk, this.m_delay, this.m_duration, this.m_intensity, this.m_repeat);
      this.m_error = 0;
    } 
    return this.m_error;
  }
  
  public int DiffuseScent(String paramString1, String paramString2, String paramString3, String paramString4, String paramString5, String paramString6, String paramString7) {
    if (this.m_error != 3) {
      this.m_type = paramString1;
      this.m_scent = paramString2;
      this.m_disk = paramString3;
      this.m_delay = paramString4;
      this.m_duration = paramString5;
      this.m_intensity = paramString6;
      this.m_repeat = paramString7;
      this.m_error = Diffuse();
    } 
    return this.m_error;
  }
  
  public int DiffuseCommand(String paramString) {
    if (this.m_error != 3) {
      this.m_type = "";
      this.m_scent = "";
      this.m_disk = "";
      this.m_delay = "";
      this.m_duration = "";
      this.m_intensity = "";
      this.m_repeat = "";
      try {
        int i = paramString.indexOf(',');
        if (i != -1) {
          this.m_type = paramString.substring(0, i);
          paramString = paramString.substring(i + 1);
          i = paramString.indexOf(',');
          if (i != -1) {
            this.m_scent = paramString.substring(0, i);
            paramString = paramString.substring(i + 1);
            i = paramString.indexOf(',');
            if (i != -1) {
              this.m_disk = paramString.substring(0, i);
              paramString = paramString.substring(i + 1);
              i = paramString.indexOf(',');
              if (i != -1) {
                this.m_delay = paramString.substring(0, i);
                paramString = paramString.substring(i + 1);
                i = paramString.indexOf(',');
                if (i != -1) {
                  this.m_duration = paramString.substring(0, i);
                  paramString = paramString.substring(i + 1);
                  i = paramString.indexOf(',');
                  if (i != -1) {
                    this.m_intensity = paramString.substring(0, i);
                    this.m_repeat = paramString.substring(i + 1);
                    this.m_error = Diffuse();
                  } else {
                    this.m_error = 1;
                  } 
                } else {
                  this.m_error = 1;
                } 
              } else {
                this.m_error = 1;
              } 
            } else {
              this.m_error = 1;
            } 
          } else {
            this.m_error = 1;
          } 
        } else {
          this.m_error = 1;
        } 
      } catch (NoSuchElementException noSuchElementException) {
        this.m_error = 1;
      } 
    } 
    return this.m_error;
    
  }
  
  public static void main(String[] args) {
		CScentDiffusionContext diffusionContext = new CScentDiffusionContext("","SCENT_4","","","10","10","");
        System.out.println("Get the version...");

        System.out.println(diffusionContext.GetExhaliaVersion());

        System.out.println("Diffuse the scent with gick");

        diffusionContext.DiffuseCommand(",SCENT_3,,,10,10,");

	}

}

